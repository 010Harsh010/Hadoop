from namenode import NameNode
from slavenode import SlaveNode
from client import Client
import time

def main():
    # Initialize NameNode (manages metadata and block assignments)
    namenode = NameNode()

    # Create 4 SlaveNodes (simulate distributed storage)
    slaves = [SlaveNode(i) for i in range(1, 5)]

    # Register SlaveNodes with the NameNode
    namenode.register_slaves(slaves)

    # Create Client (used to interact with NameNode and SlaveNodes)
    client = Client(namenode, slaves)

    # Display CLI menu
    print("HDFS Simulation CLI")
    print("Commands:")
    print("  add <file_path>         - Add file to HDFS")
    print("  read <file_name> <out>  - Read and reconstruct file")
    print("  list                    - List stored files")
    print("  exit                    - Exit CLI")

    # Start interactive CLI loop
    while True:
        try:
            # Read command from user
            cmd = input("HDFS> ").strip()
            if not cmd:
                continue
            parts = cmd.split()
            command = parts[0].lower()

            # Handle 'add' command: Upload a file to HDFS
            if command == "add":
                if len(parts) < 2:
                    print("Usage: add <file_path>")
                    continue
                client.add_file(parts[1])

            # Handle 'read' command: Read and reconstruct file from HDFS
            elif command == "read":
                if len(parts) < 3:
                    print("Usage: read <file_name> <output_file>")
                    continue

                # Simulate progress bar (loading effect)
                for i in range(1, 6):
                    print(f"Reading file... {i*20}%", end="\r")
                    time.sleep(0.5)

                # Perform actual read operation
                client.read_file(parts[1], parts[2])

            # Handle 'list' command: Show stored files in HDFS
            elif command == "list":
                files = namenode.metadata.keys()
                if files:
                    print("Files in HDFS:")
                    for f in files:
                        print(f" - {f}")
                else:
                    print("No files stored in HDFS.")

            # Handle 'exit' command: Exit the CLI
            elif command == "exit":
                print("Exiting HDFS CLI...")
                break

            # Handle invalid commands
            else:
                print("Unknown command. Type 'add', 'read', 'list', or 'exit'.")

        except KeyboardInterrupt:
            print("\nExiting HDFS CLI...")
            break
        except Exception as e:
            print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
