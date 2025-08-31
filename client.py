import os

# Define block size as 32 MB (like HDFS default block size)
BLOCK_SIZE = 32 * 1024 * 1024  # 32 MB

class Client:
    def __init__(self, namenode, slaves):
        """
        Client interacts with NameNode and SlaveNodes to upload and download files.
        :param namenode: Instance of NameNode
        :param slaves: List of SlaveNode objects
        """
        self.namenode = namenode
        # Convert list of slaves to dictionary for quick access by slave_id
        self.slaves = {slave.node_id: slave for slave in slaves}

    def add_file(self, filepath):
        """
        Splits the file into blocks and stores them across SlaveNodes.
        :param filepath: Path of the local file to be uploaded to HDFS
        """
        if not os.path.exists(filepath):
            print(f"File {filepath} does not exist.")
            return

        # Get the file size in bytes
        file_size = os.path.getsize(filepath)
        # Calculate number of blocks required for this file
        block_count = (file_size + BLOCK_SIZE - 1) // BLOCK_SIZE

        # Request NameNode to assign slaves for storing each block
        assignments = self.namenode.assign_slaves_for_file(os.path.basename(filepath), block_count)

        # Read file in chunks (BLOCK_SIZE) and send to respective SlaveNodes
        with open(filepath, 'rb') as f:
            for assign in assignments:
                block_data = f.read(BLOCK_SIZE)  # Read next 32 MB chunk
                slave_id = assign['slave_id']    # SlaveNode ID where this block goes
                block_num = assign['block_num']  # Block sequence number
                # Store the block on the assigned SlaveNode
                self.slaves[slave_id].store_block(os.path.basename(filepath), block_num, block_data)
                print(f"Stored block {block_num} in SlaveNode {slave_id}")

    def read_file(self, filename, output_path):
        """
        Fetches file blocks from SlaveNodes and reconstructs the original file.
        :param filename: Name of the file in HDFS
        :param output_path: Path where the reconstructed file will be saved locally
        """
        # Get block assignment details from NameNode
        assignments = self.namenode.get_blocks_for_file(filename)
        if not assignments:
            print("File not found in metadata.")
            return

        # Open output file in binary write mode
        with open(output_path, 'wb') as out:
            # Sort blocks by block number to maintain correct order
            for assign in sorted(assignments, key=lambda x: x['block_num']):
                slave_id = assign['slave_id']
                block_num = assign['block_num']
                # Fetch the block data from the appropriate SlaveNode
                block_data = self.slaves[slave_id].fetch_block(filename, block_num)
                if block_data:
                    out.write(block_data)
                    print(f"Fetched block {block_num} from SlaveNode {slave_id}")
                else:
                    print(f"Block {block_num} missing from SlaveNode {slave_id}")

        print(f"File reconstructed at {output_path}")
