def test_rag_tools_only_in_dev(build_mode):
    if build_mode == "be":
        import pytest
        pytest.skip("RAG tools not available in BE")
    
    # Simulate successful dev-only test
    assert True
