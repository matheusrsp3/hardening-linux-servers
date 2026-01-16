from core.file_audit import FileAudit

files_audit = [
    '/etc/passwd',
    '/etc/shadow',
]

files = FileAudit(files_audit)
files.check_permissions(mode='0023')