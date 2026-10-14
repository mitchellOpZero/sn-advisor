"""Validate the shipped plugin metadata and read-only configs without dependencies."""

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = Path("providers/claude/plugin")
MODES = {"manual", "advisor_first", "passive", "disabled"}


def validate_config(config):
    """Return errors for a complete shipped config, not a partial user override."""
    errors = []
    if not isinstance(config, dict):
        return ["config must be an object"]
    if not isinstance(config.get("mode"), str) or config["mode"] not in MODES:
        errors.append("mode must be manual, advisor_first, passive, or disabled")
    for section, limit in (
        ("web_search", "max_results_per_tier"),
        ("instance_readonly", "max_records_per_query"),
    ):
        settings = config.get(section)
        if not isinstance(settings, dict):
            errors.append(f"{section} must be an object")
            continue
        if type(settings.get("enabled")) is not bool:
            errors.append(f"{section}.enabled must be a boolean")
        value = settings.get(limit)
        if type(value) is not int or value <= 0:
            errors.append(f"{section}.{limit} must be a positive integer")
        if section == "instance_readonly":
            if settings.get("http_methods_allowed") != ["GET"]:
                errors.append("instance_readonly.http_methods_allowed must be ['GET']")
    return errors


def validate_repository(root=ROOT):
    errors = []

    def read_json(path):
        try:
            return json.loads((root / path).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            errors.append(f"{path}: {error}")
            return None

    for path in (
        PLUGIN / "references/default-resources.json",
        Path("examples/sn-advisor.config.example.json"),
    ):
        config = read_json(path)
        errors.extend(f"{path}: {error}" for error in validate_config(config))

    manifest = read_json(PLUGIN / ".claude-plugin/plugin.json")
    marketplace = read_json(Path(".claude-plugin/marketplace.json"))
    if not isinstance(manifest, dict):
        errors.append("plugin manifest must be an object")
    elif not isinstance(marketplace, dict):
        errors.append("marketplace must be an object")
    else:
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
            errors.append("marketplace must contain the single advisor plugin")
        else:
            entry = plugins[0]
            for key in ("name", "version"):
                if not isinstance(manifest.get(key), str) or not manifest[key]:
                    errors.append(f"plugin {key} must be a nonempty string")
                elif entry.get(key) != manifest[key]:
                    errors.append(f"marketplace plugin {key} does not match manifest")
            if entry.get("source") != f"./{PLUGIN.as_posix()}/":
                errors.append("marketplace source must point to the installable plugin")

    for path in (
        "commands/sn-advisor.md",
        "references/configuration-policy.md",
        "references/default-resources.json",
        "references/source-trust-policy.md",
        "references/task-resource-matrix.md",
        "references/instance-context-matrix.md",
        "skills/sn-advisor-router/SKILL.md",
        "skills/sn-instance-readonly/SKILL.md",
        "skills/sn-source-ranking/SKILL.md",
        "skills/sn-output-templates/SKILL.md",
    ):
        if not (root / PLUGIN / path).is_file():
            errors.append(f"missing plugin file: {path}")
    return errors


if __name__ == "__main__":
    problems = validate_repository()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print("Plugin metadata and shipped read-only configurations are valid.")
