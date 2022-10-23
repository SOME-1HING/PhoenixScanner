from PhoenixScanner import Phoenix

scanner = Phoenix()

user_id = 65465498
is_gban, reason = scanner.gban_check(user_id)
print(f'''
user_id: {user_id}
is_gban: {is_gban}
reason: {reason}
''')