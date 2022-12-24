from models.language import Language

def test_language_model_documentation():
    language = Language(1, 'python', 'source_file', 'compile_cmd', 'run_cmd')
    assert language.__doc__ != None