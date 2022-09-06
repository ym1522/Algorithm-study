# IP주소에는 IPv4와 IPv6의 두 가지 체계가 있습니다.
# IPv4는 "A.B.C.D" 형태의 IP를 말하며, A, B, C, D는 0이상 255이하의 정수입니다.
# IPv6은 "A:B:C:D:E:F:G:H" 형태의 IP를 말하며, A, B, C, D, E, F, G, H는 4자리의 16진수 수입니다.
# IP가 주어졌을 때, 해당 IP가 IPv4 형식인지 IPv6 형식인지 출력하세요.

import sys

IP = sys.stdin.readline()
IPv4 = IP.split('.')
IPv6 = IP.split(':')

if len(IPv4) == 4:
    print("IPv4")
    
if len(IPv6) == 8:
    print("IPv6")