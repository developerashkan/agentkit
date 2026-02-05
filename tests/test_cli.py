from agentkit.cli.main import scaffold_project


def test_scaffold_project(tmp_path):
    root = scaffold_project(str(tmp_path / "starter"))
    assert (root / "agents").exists()
    assert (root / "skills").exists()
