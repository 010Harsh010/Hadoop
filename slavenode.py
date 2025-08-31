import os

class SlaveNode:
    def __init__(self, node_id, storage_dir="slave_storage"):
        # Each SlaveNode gets a unique ID and its own storage directory
        self.node_id = node_id
        # Create a subdirectory for this node inside the main storage directory
        self.storage_dir = os.path.join(storage_dir, f"node_{node_id}")
        os.makedirs(self.storage_dir, exist_ok=True)  # Ensure directory exists

    def store_block(self, filename, block_num, data):
        """
        Store a block of a file in the slave node.
        :param filename: Name of the file this block belongs to
        :param block_num: The block number (sequence in the file)
        :param data: The actual binary data of the block
        """
        # Create a directory for the file inside this node's storage
        file_dir = os.path.join(self.storage_dir, filename)
        os.makedirs(file_dir, exist_ok=True)

        # Path for this specific block
        block_path = os.path.join(file_dir, f"block_{block_num}")
        
        # Write the block data to the file in binary mode
        with open(block_path, 'wb') as f:
            f.write(data)

    def fetch_block(self, filename, block_num):
        """
        Fetch a block of a file from the slave node.
        :param filename: Name of the file
        :param block_num: Block number to retrieve
        :return: Binary data of the block or None if block not found
        """
        # Path to the requested block
        block_path = os.path.join(self.storage_dir, filename, f"block_{block_num}")
        
        # Check if block exists, then read and return it
        if os.path.exists(block_path):
            with open(block_path, 'rb') as f:
                return f.read()
        return None
