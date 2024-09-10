
import os
import subprocess
import sys

def run_openscap_scan():
    print("Running OpenSCAP scan...")
    subprocess.run(["docker-compose", "run", "openscap", "/scap/run_scan.sh"])

def setup_openvas():
    print("Setting up OpenVAS...")
    subprocess.run(["docker-compose", "up", "-d", "openvas"])
    print("OpenVAS is now running. Access the web interface at https://localhost")
    print("Default credentials: admin / admin")
    print("Please change the password immediately after first login.")

def main():
    if not os.path.exists("docker-compose.yml"):
        print("docker-compose.yml not found. Please ensure you're in the correct directory.")
        sys.exit(1)

    while True:
        print("\n1. Run OpenSCAP scan")
        print("2. Setup/Start OpenVAS")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            run_openscap_scan()
        elif choice == "2":
            setup_openvas()
        elif choice == "3":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
