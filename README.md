# 스트림릿 및 모델링 코드 저장용 리포지토리

### 스트림릿 폴더에 스트림릿 코드 있습니다.

---

0221 commit 메모

eee, fff 파일 추가  
채팅 UI를 추가함, 현재는 입력값을 되풀이만 하고있음, 여기에 모델을 넣으면 될 것 같음음  
초기 화면에서는 전체화면의 챗봇이었다가  
"추천" 이라는 글자를 인식하면 UI가 오른쪽으로 이동하고  
왼쪽에는 추천곡이 뜨는 형식으로 만들어봄

한계점 + TODO

1. 애니메이션을 넣어서 부드럽게 해보려 했으나 챗봇에서는 애니메이션이 안먹히고 있음
2. 초기 화면에서는 양쪽으로 벌어져 있는 채팅창이 아니라 가운데로 몰려있으면 좋겠는데 저 초기에 올라오는 메세지 때문에 안되고있음
3. 디자인적 요소는 아직 넣지 않음
4. 채팅이 쌓여서 스크롤이 내려갈 때 채팅박스가 따로 스크롤이 되었음 좋겠는데 화면 전체로 스크롤 되는중
5. 다시 확인해보니까 추천해준 다음에 채팅이 이상하게 나옴 고쳐야함

---

0220 commit 메모

사이드바는 직접적으로 코드로 컨트롤이 불가능함  
가운데에 있다가 추천이 되면 왼쪽으로 이동하고 오른쪽에 리스트를 주루루룩 하고싶었으나  
왼쪽으로 이동하는게 좀 어려움  
일단 양옆으로 정렬하는건 알아냈음 이거를 기반으로  
col1, col2로 나눠서 하면 좋을 것 같음  
추천해주기 전에는 가운데 정렬이다가  
추천해줄때는 col1, 2로 나눠서 나뉘는걸로 하면 좋을 것같음  
근데 애니메이션까지 넣어서 나누는게 가능할지 모르겠음

---
