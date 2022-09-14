# 가영이가 사용하는 텍스트 에디터에는 "찾아 바꾸기"라는 기능이 있습니다. 찾고 싶은 내용과 바꾸고 싶은 내용이 입력되면 커서 위치와 같거나 그 뒤에 있는 위치에서 해당 내용을 찾아서 바꾸는 기능입니다. 
# 조금 더 구체적으로 설명하면, 현재 텍스트 에디터에 입력된 전체 내용을 S, 현재 커서 위치를 cur (0 ≤ cur ≤ |S|), 찾고 싶은 내용을 s, 바꾸고 싶은 내용을 t라고 했을 때, S[i .. i+|s|-1] = s를 만족하는 최소의 i (i ≥ cur)를 찾아서 t로 바꾸면 됩니다. 
# 만약 해당하는 i가 존재하지 않는 경우, 아무 동작도 하지 않습니다. 처음에 텍스트 에디터에 입력되어 있던 내용과 찾아 바꾸기를 사용한 이력이 입력될 때, 텍스트 에디터에 입력되어 있던 내용이 어떻게 변해있을 지 알아내는 프로그램을 작성해주세요.

# 예제 입력1
# qwertyuiop
# 3
# wer ab 1
# tyu ccccc 2
# qab ii 5
# 예제 출력1
# qabtyuiop
# qabccccciop
# qabccccciop

# 예제 입력2
# yupvtdzblcnzgrjkvqlpqogapttlxtlrtbfbpgfizookpezifn
# 10
# qogapttlxtlrtbfbpgfizookpezifn kivmydapagldxyeojblvzafhopykttxzsuoc 5
# txzsuoc jzcs 8
# yeojblvzafhopyktjzcs sabziowzcdogdwfiioyfyyizcoytitblefvjipplv 11
# zcdogdwfiioyfyyizcoytitblefvjipplv fjxbvfhu 31
# vmydapagldxsabziowfjxbvfhu zfmuonomdmclrbmreydwhdnb 25
# vfhu hhezpgjaqtpxsgmrqzw 11
# gldxsabziowfjxbhhezpgjaqtpxsgmrqzw yvrfhqrifipesohifitbih 11
# h dtjhqxcwzsriljplurilhmiwjskqnuhx 50
# rifipesohifitbidtjhqxcwzsriljplurilhmiwj hkbehkmdtywxxovzchwanhuysnogcgifdupwijic 4
# vtdzblcnzgrjkvqlpkivmydapayvrf lkkctkuwgsabugcafjbebsjspejonjivyxexjiz 25
# 예제 출력2
# yupvtdzblcnzgrjkvqlpkivmydapagldxyeojblvzafhopykttxzsuoc
# yupvtdzblcnzgrjkvqlpkivmydapagldxyeojblvzafhopyktjzcs
# yupvtdzblcnzgrjkvqlpkivmydapagldxsabziowzcdogdwfiioyfyyizcoytitblefvjipplv
# yupvtdzblcnzgrjkvqlpkivmydapagldxsabziowfjxbvfhu
# yupvtdzblcnzgrjkvqlpkivmydapagldxsabziowfjxbvfhu
# yupvtdzblcnzgrjkvqlpkivmydapagldxsabziowfjxbhhezpgjaqtpxsgmrqzw
# yupvtdzblcnzgrjkvqlpkivmydapayvrfhqrifipesohifitbih
# yupvtdzblcnzgrjkvqlpkivmydapayvrfhqrifipesohifitbidtjhqxcwzsriljplurilhmiwjskqnuhx
# yupvtdzblcnzgrjkvqlpkivmydapayvrfhqhkbehkmdtywxxovzchwanhuysnogcgifdupwijicskqnuhx
# yupvtdzblcnzgrjkvqlpkivmydapayvrfhqhkbehkmdtywxxovzchwanhuysnogcgifdupwijicskqnuhx

# 입력값 설명
# 첫째 줄에 알파벳 소문자로만 이루어진 문자열 S가 입력됩니다. (1 ≤ |S| ≤ 50)
# 둘째 줄에 찾아바꾸기를 사용한 횟수 N이 입력됩니다. (1 ≤ N ≤ 10)
# 셋째 줄부터 N개의 줄에 걸쳐서 문제에서 설명한 s, t, cur이 공백으로 구분되어 입력됩니다. (1 ≤ |s|, |t| ≤ 50, 0 ≤ cur ≤ |S|)

# 출력값 설명
# 총 N개의 줄을 출력합니다.
# i번째 줄에, i번째 찾아바꾸기까지 시행했을 때 문자열의 모습을 출력합니다.