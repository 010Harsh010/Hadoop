# HDFS Simulation in Python

This project simulates the **Hadoop Distributed File System (HDFS)** in Python.  
It demonstrates how a **NameNode** manages metadata and how files are split into blocks and distributed across multiple **SlaveNodes**.

---

## ✅ Features
- **NameNode**
  - Maintains metadata for files (which blocks are stored on which SlaveNode).
  - Handles slave registration.
  - Assigns file blocks to different SlaveNodes in a round-robin fashion.
  - Stores metadata in `metadata.json`.

- **SlaveNode**
  - Stores file blocks.
  - Each block is identified by a `block_num`.

- **Client**
  - Reads a large file.
  - Splits it into blocks (e.g., 32 MB per block).
  - Sends the blocks to the NameNode for assignment.
  - Stores blocks on respective SlaveNodes.

---

## ✅ Project Structure
HDFS-Simulation/
│
├── namenode.py # NameNode implementation
├── slavenode.py # SlaveNode implementation
├── client.py # Client for reading/writing files
├── metadata.json # Metadata for file-block mapping
└── README.md # Project documentation


---

## ✅ How It Works
1. **NameNode**:
   - Keeps track of which file blocks are stored on which SlaveNodes.
   - Saves metadata in `metadata.json`.

2. **SlaveNodes**:
   - Store file blocks assigned by the NameNode.

3. **Client**:
   - Reads a file.
   - Splits it into blocks.
   - Uploads blocks to SlaveNodes based on NameNode assignment.
   - Can retrieve the file by downloading blocks and merging them.

---

## ✅ Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/hdfs-simulation.git
cd hdfs-simulation
