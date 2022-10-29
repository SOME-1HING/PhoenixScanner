from PhoenixScanner import Phoenix

Scanner = Phoenix("token")

print(Scanner.gban_check(82))
"Output: {'user_id': 82, 'is_gban': True, 'reason': 'cwsck', 'scanner': 23123}"

print(Scanner.gban_revert(82))
"Output: 'Deleted'"

print(Scanner.gban_scan(82, "cwsck", 23123))
"Output: 'Done"

print(Scanner.token_gen())
'Output: "RED7-m201vbup6qefssf7ssqqbn"'

print(Scanner.token_revoke("RED7-m201vbup6qefssf7ssqqbn"))
'Output: "Deleted"'