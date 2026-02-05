import json

from agentkit.skills.compat import load_manifest, render_skill_template


def test_render_skill_template_contains_required_fields(tmp_path):
    manifest = render_skill_template("demo")
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    loaded = load_manifest(manifest_path)
    assert loaded.name == "demo"
    assert loaded.entrypoint.endswith(":run")
