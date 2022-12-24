from  dataclasses import dataclass

@dataclass
class Language:
    """A data class used to represent a programming Language

    Note:
        Only compiled languages like C, C++, etc have a compile command.
        Once the code has been compiled then the run command can be used.
        Innterpreted languages don't have a compile command. They can be
        run directly using the run command.

    Attributes:
        id (int): A unique identifier for a language
        name (str):  Name of the language
        source_file (str): The file containing the source code
        compile_cmd (str): Compile command for compiled languages
        run_cmd: The run command used to run the code
    
    """

    id: int
    name: str
    source_file: str
    compile_cmd: str
    run_cmd: str