import sys

def run_potato_code(file_path):
    potato_basket = {}

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return

    for line in lines:
        line = line.strip()
        
        if not line or line.startswith("#"):
            continue
            
        parts = line.split(" ", 2)
        command = parts[0]

        if command == "PLANT":
            continue
            
        elif command == "BAKE":
            var_name = parts[1]
            var_value = parts[2]
            if var_value.startswith('"') and var_value.endswith('"'):
                var_value = var_value[1:-1]
            potato_basket[var_name] = var_value

        elif command == "MASH":
            target = line[5:].strip()
            if target.startswith('"') and target.endswith('"'):
                print(target[1:-1])
            elif target in potato_basket:
                print(potato_basket[target])
            else:
                print(target)

        elif command == "HARVEST":
            break

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        run_potato_code(sys.argv[1])
