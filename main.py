from core.file_audit import FileAudit

files_audit = [
    '/etc/passwd',
    '/etc/shadow',
    '/home/mcarvalho/github/hardening-linux-servers/matheus.link',
]

files = FileAudit(files_audit)
list_of_verified_files = files.check_permissions(mode='0640')

for file in list_of_verified_files:
    # if not file[0]:
    files.change_permissions(mode='0640', filepath=file[1])