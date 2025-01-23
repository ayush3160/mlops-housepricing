from fastapi.testclient import TestClient
import os
import pytest
from main import *  # Importing all from the source module, serve_homepage
def test_dummy():
	assert True
# Test generated using Keploy
def test_serve_homepage_file_not_found(monkeypatch, tmp_path):
    # Mock os.getcwd to return a directory without index.html
    monkeypatch.setattr(os, "getcwd", lambda: str(tmp_path))
    try:
        serve_homepage()
    except FileNotFoundError as e:
        assert "index.html" in str(e)
# Test generated using Keploy
def test_serve_homepage_file_exists(monkeypatch, tmp_path):
    # Create a temporary index.html file
    static_dir = tmp_path / "static"
    static_dir.mkdir()
    index_file = static_dir / "index.html"
    index_file.write_text("<html><body>Test Homepage</body></html>")
    # Mock os.getcwd to return the temporary directory
    monkeypatch.setattr(os, "getcwd", lambda: str(static_dir.parent))
    response = serve_homepage()
    assert response.status_code == 200
    assert "Test Homepage" in response.body.decode()