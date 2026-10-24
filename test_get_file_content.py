from functions.get_file_content import get_file_content

def test() -> None:
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    file_name = "main.py"
    result = get_file_content("calculator", file_name)
    print(f"Result for current file {file_name}:\n{result}")
    #print({result}) if 'Error:' in result else print(f"{file_name} length: {len(result)}\n{file_name} truncated: {'truncated' in result}")
    print("")

    file_name = "pkg/calculator.py"
    result = get_file_content("calculator", file_name)
    print(f"Result for current file {file_name}:\n{result}")
    #print({result}) if 'Error:' in result else print(f"{file_name} length: {len(result)}\n{file_name} truncated: {'truncated' in result}")
    print("")

    file_name = "/bin/cat"
    result = get_file_content("calculator", file_name)
    print(f"Result for current file {file_name}:\n{result}")
    #print({result}) if 'Error' in result else print(f"{file_name} length: {len(result)}\n{file_name} truncated: {'truncated' in result}")
    print("")

    file_name = "pkg/does_not_exist.py"
    result = get_file_content("calculator", file_name)
    print(f"Result for current file {file_name}:\n{result}")
    #print(f"{result}") if 'Error' in result else print(f"{file_name} length: {len(result)}\n{file_name} truncated: {'truncated' in result}")
    print("")


if __name__ == "__main__":
    test()
