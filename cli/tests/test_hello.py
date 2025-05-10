import subprocess

def test_hello_world(tmp_path, monkeypatch):
    # install the CLI package in editable mode
    # here we assume entrypoint 'launchkit' is on PATH
    result = subprocess.run(["launchkit", "hello", "world"], capture_output=True, text=True)
    assert "Hello, LaunchKit!" in result.stdout
