files = ["security.log", "users.csv", "access.log", "report.txt"]
log_files = [file for file in files if file.endswith(".log")]
print(log_files)