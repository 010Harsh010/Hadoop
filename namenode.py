import json
import os

class NameNode:
    def __init__(self, metadata_file="metadata.json"):
        # Path to metadata file where file-block assignments are stored
        self.metadata_file = metadata_file
        # Dictionary to hold metadata in memory (filename -> block info)
        self.metadata = {}
        # List of registered slave nodes
        self.slaves = []
        # Round-robin index to distribute blocks across slaves
        self.slave_index = 0
        # Load existing metadata if available
        self.load_metadata()

    def register_slaves(self, slaves):
        # Register the list of slave nodes in the cluster
        self.slaves = slaves

    def load_metadata(self):
        # Load metadata from JSON file if it exists
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r') as f:
                self.metadata = json.load(f)
        else:
            # If no file exists, initialize empty metadata
            self.metadata = {}

    def save_metadata(self):
        # Save the current metadata dictionary to the JSON file
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f)

    def assign_slaves_for_file(self, filename, block_count):
        # Assign blocks of a file to different slaves using round-robin
        if filename in self.metadata:
            # If file is already assigned, return existing assignments
            return self.metadata[filename]

        block_assignments = []
        for block_num in range(block_count):
            # Pick a slave in round-robin fashion
            slave = self.slaves[self.slave_index]
            self.slave_index = (self.slave_index + 1) % len(self.slaves)
            # Store which slave will hold which block number
            block_assignments.append({'slave_id': slave.node_id, 'block_num': block_num})

        # Save assignments in metadata and persist to file
        self.metadata[filename] = block_assignments
        self.save_metadata()
        return block_assignments

    def get_blocks_for_file(self, filename):
        # Retrieve block assignments for a given file
        return self.metadata.get(filename, [])
