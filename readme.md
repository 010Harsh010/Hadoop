# HDFS Simulation in Python

## 📌 Introduction
This project simulates a simplified **Hadoop Distributed File System (HDFS)** using **Python**. It demonstrates how files are split into blocks, distributed across multiple nodes (SlaveNodes), and managed by a central NameNode. It also provides an **interactive CLI** to perform file operations like **add**, **read**, and **list**.

---

## ✅ Features
- **File Upload**: Splits large files (e.g., 100 MB) into 32 MB blocks and stores them on different SlaveNodes.
- **File Retrieval**: Reconstructs the original file by fetching blocks in the correct order.
- **Metadata Management**: Stores file-to-block mapping in a JSON file (`metadata.json`), allowing persistence across restarts.
- **Round-Robin Block Distribution**: Distributes file blocks evenly across available SlaveNodes.
- **Interactive CLI**: Commands to add, read, and list files in the HDFS simulation.

---

## 🔍 System Architecture

### **Components**
- **NameNode**:
  - Manages metadata (file names, block locations).
  - Assigns blocks to SlaveNodes using **round-robin**.
  - Stores metadata persistently in `metadata.json`.

- **SlaveNode**:
  - Stores actual file blocks in its own directory.
  - Retrieves blocks when requested by the client.

- **Client**:
  - Uploads files by contacting NameNode for block assignments.
  - Reads files by fetching blocks from respective SlaveNodes.
  - Provides CLI for user interaction.

---

## 🛠️ Technologies Used
- **Python 3**
- **JSON** for metadata storage
- **OS module** for directory and file handling

---

## 📂 Project Structure

hdfs-simulation/
│
├── namenode.py # Handles metadata and block assignments
├── slavenode.py # Handles block storage and retrieval
├── client.py # Handles file operations (upload & download)
├── cli.py # Interactive HDFS CLI
├── metadata.json # Stores file-to-block mapping (auto-generated)
└── README.md # Documentation


---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/010Harsh010/Hadoop
   cd hdfs-simulation
   python run.py
   
## ⚙️ HDFS CLI
    ```bash
    Available Commands


    add <file_path> → Upload a file to HDFS.
    read <file_name> <output_path> → Retrieve and reconstruct a file.
    list → List all stored files in HDFS.
    exit → Exit the CLI.

    ```bash
    Add Commands

    HDFS> add sample.txt
    Stored block 0 in SlaveNode 1
    Stored block 1 in SlaveNode 2
    Stored block 2 in SlaveNode 3
    Stored block 3 in SlaveNode 4

    ```bash
        Read Commands

        HDFS> read sample.txt output.txt
        Reading file... 100%
        Fetched block 0 from SlaveNode 1
        Fetched block 1 from SlaveNode 2
        Fetched block 2 from SlaveNode 3
        Fetched block 3 from SlaveNode 4
        File reconstructed at output.txt


    ```bash
        List Commands
        
        HDFS> list
        Files in HDFS:
        - sample.txt