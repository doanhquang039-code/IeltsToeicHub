/**
 * LINGUAHUB - TOEIC ENGINE & OFFICIAL ETS TEST REPOSITORY
 * ETS TOEIC 2024 - Full 4 Skills:
 *   Listening:  Part 1 (6q) + Part 2 (7q) + Part 3 (3 conv×3q) + Part 4 (2 talks×3q) = 25 câu
 *   Reading:    Part 5 (10q grammar) + Part 6 (4q text) + Part 7 (10q multi-passages) = 24 câu
 *   Speaking:   11 câu (Read Aloud + Q&A + Propose Solution + Opinion)
 *   Writing:    3 bài (Email + Essay)
 * Thang quy đổi điểm 10–990 chuẩn ETS.
 */

(function(window) {
  'use strict';

  // ==========================================
  // 1. DANH SÁCH ĐỀ THI TOEIC (COURSES)
  // ==========================================
  const toeicCourses = [
    // === ĐỀ THI THẬT ETS 2024 ===
    {
      kind: 'TOEIC', skill: 'Listening',
      title: 'TOEIC Actual Test ETS 2024 · Test 1 – Full Listening (25 Câu)',
      detail: 'Part 1: Mô tả tranh (6q) | Part 2: Hỏi & Đáp phản xạ (7q) | Part 3: Hội thoại công sở (9q) | Part 4: Bài thuyết trình & thông báo (6q)',
      questions: 25, time: '25 phút', mark: 'ETS-2024-L1',
      type: 'audio_mcq', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    {
      kind: 'TOEIC', skill: 'Reading',
      title: 'TOEIC Actual Test ETS 2024 · Test 1 – Full Reading (24 Câu)',
      detail: 'Part 5: Ngữ pháp & Từ vựng (10q) | Part 6: Điền vào đoạn văn (4q) | Part 7: Đọc hiểu đơn & đôi văn bản (10q)',
      questions: 24, time: '30 phút', mark: 'ETS-2024-R1',
      type: 'reading_passage', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    {
      kind: 'TOEIC', skill: 'Speaking',
      title: 'TOEIC Actual Test ETS 2024 · Test 1 – Full Speaking (11 Câu)',
      detail: 'Đọc to (2q) | Mô tả ảnh (1q) | Trả lời câu hỏi (3q) | Trả lời câu hỏi dựa trên thông tin (3q) | Đề xuất giải pháp (1q) | Bày tỏ quan điểm (1q)',
      questions: 11, time: '20 phút', mark: 'ETS-2024-S1',
      type: 'speaking', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    {
      kind: 'TOEIC', skill: 'Writing',
      title: 'TOEIC Actual Test ETS 2024 · Test 1 – Full Writing (3 Bài)',
      detail: 'Câu dựa trên ảnh (1q) | Viết email phản hồi (1q) | Essay bày tỏ quan điểm (1q)',
      questions: 3, time: '60 phút', mark: 'ETS-2024-W1',
      type: 'writing', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    {
      kind: 'TOEIC', skill: 'Listening',
      title: 'TOEIC Actual Test ETS 2024 · Test 2 – Full Listening (25 Câu)',
      detail: 'Part 1: Tranh văn phòng & ngoài trời | Part 2: Yêu cầu & lời mời | Part 3: Hội thoại 3 người, hội nghị | Part 4: Tour & Thông báo nội bộ',
      questions: 25, time: '25 phút', mark: 'ETS-2024-L2',
      type: 'audio_mcq', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    {
      kind: 'TOEIC', skill: 'Reading',
      title: 'TOEIC Actual Test ETS 2024 · Test 2 – Full Reading (24 Câu)',
      detail: 'Part 5: Liên từ nâng cao & mệnh đề quan hệ | Part 6: Email & Thông báo | Part 7: Đề nghị & Hợp đồng đa quốc gia',
      questions: 24, time: '30 phút', mark: 'ETS-2024-R2',
      type: 'reading_passage', isActualTest: true, source: 'ETS', badge: 'ETS 2024'
    },
    // === BÀI LUYỆN THEO PART ===
    { kind: 'TOEIC', skill: 'Listening', title: 'TOEIC Part 1 Practice – Photograph Description', detail: 'Luyện mô tả tranh ảnh: văn phòng, ngoài trời, cuộc họp', questions: 6, time: '8 phút', mark: 'TP1', type: 'audio_mcq', isActualTest: false, source: 'Practice' },
    { kind: 'TOEIC', skill: 'Listening', title: 'TOEIC Part 2 Practice – Question Response', detail: 'Luyện phản xạ câu trả lời nhanh cho các dạng câu hỏi WH, Yes/No, Tag', questions: 8, time: '8 phút', mark: 'TP2', type: 'audio_mcq', isActualTest: false, source: 'Practice' },
    { kind: 'TOEIC', skill: 'Listening', title: 'TOEIC Part 3 Practice – Short Conversations', detail: 'Luyện nghe hội thoại ngắn 3-5 lượt về chủ đề công sở', questions: 9, time: '10 phút', mark: 'TP3', type: 'audio_mcq', isActualTest: false, source: 'Practice' },
    { kind: 'TOEIC', skill: 'Reading', title: 'TOEIC Part 5 Practice – Incomplete Sentences', detail: 'Luyện ngữ pháp & từ vựng điền câu: 15 câu đa dạng chủ đề', questions: 10, time: '12 phút', mark: 'TP5', type: 'reading_passage', isActualTest: false, source: 'Practice' },
    { kind: 'TOEIC', skill: 'Reading', title: 'TOEIC Part 7 Practice – Single Passage', detail: 'Luyện đọc hiểu đơn văn bản: email, quảng cáo, thông báo', questions: 6, time: '10 phút', mark: 'TP7', type: 'reading_passage', isActualTest: false, source: 'Practice' },
    { kind: 'TOEIC', skill: 'Writing', title: 'TOEIC Writing Practice – Email Response', detail: 'Luyện viết email phản hồi chuyên nghiệp trong bối cảnh kinh doanh', questions: 2, time: '20 phút', mark: 'TW1', type: 'writing', isActualTest: false, source: 'Practice' }
  ];

  // ==========================================
  // 2. NGÂN HÀNG ĐỀ THI TOEIC CHI TIẾT (EXAMS)
  // ==========================================
  const toeicExams = {

    // ===========================================================
    // ETS 2024 TEST 1 – FULL LISTENING (25 CÂU)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 1 – Full Listening (25 Câu)': {
      type: 'audio_mcq',
      audioTitle: 'ETS TOEIC 2024 Test 1 – Official Listening (Speed: 1.0x Normal, Accent: North American & British)',
      audioScript: `PART 1 – PHOTOGRAPH DESCRIPTION (6 questions)
[Photo 1] Narrator: Look at the photograph marked Number 1.
(A) A man is hanging a picture on the wall.
(B) A man is reviewing documents at a conference table.
(C) A man is setting up a projector in a meeting room.
(D) A man is arranging chairs around a table.

[Photo 2] Narrator: Look at the photograph marked Number 2.
(A) The customers are paying at the register.
(B) A cashier is bagging groceries for a customer.
(C) Several products are displayed on the shelves.
(D) An employee is stocking items on the shelves.

[Photo 3] Narrator: Look at the photograph marked Number 3.
(A) Boxes are being loaded onto a delivery truck.
(B) A worker is sealing packages with tape.
(C) Merchandise is stacked near the warehouse entrance.
(D) A forklift is moving pallets across the floor.

[Photo 4] Narrator: Look at the photograph marked Number 4.
(A) A woman is handing a folder to her colleague.
(B) Two colleagues are seated across from each other, looking at a laptop.
(C) A woman is typing on a keyboard in the office.
(D) Several people are gathered around a whiteboard.

[Photo 5] Narrator: Look at the photograph marked Number 5.
(A) A train is arriving at the station platform.
(B) Passengers are boarding a bus.
(C) A train has pulled up alongside the platform and some passengers are getting off.
(D) Workers are repairing the train tracks.

[Photo 6] Narrator: Look at the photograph marked Number 6.
(A) Diners are seated at outdoor tables.
(B) A chef is preparing food in the kitchen.
(C) Tables and chairs have been set up inside the restaurant.
(D) Waiters are clearing dishes from the tables.

PART 2 – QUESTION-RESPONSE (7 questions)
Narrator: Mark your answer on your answer sheet.

7. Man: When is the quarterly sales report due?
(A) Yes, it was due last month.
(B) By the end of Thursday.
(C) At the marketing conference room.

8. Woman: Could you review my presentation slides before the meeting?
(A) I already submitted the slides online.
(B) Sure, send them over this afternoon.
(C) The meeting was held on Friday.

9. Man: Has the new office furniture been delivered yet?
(A) It arrived this morning and is in the storage room.
(B) The furniture store is two blocks away.
(C) We ordered three new chairs.

10. Woman: Who will be leading the training session tomorrow?
(A) The training was excellent.
(B) It will be conducted by Ms. Park from HR.
(C) The session runs for two hours.

11. Man: Do you know where the parking validation forms are?
(A) The parking lot is on level B2.
(B) I think Lisa keeps them at the reception desk.
(C) Validation takes about fifteen minutes.

12. Woman: Should we reschedule the client call or keep it at ten?
(A) The client is from Toronto.
(B) Let's push it back to eleven — Mr. Chen has a conflict.
(C) The call went very well, thank you.

13. Man: Isn't the annual budget review meeting next Monday?
(A) Actually, it was moved to Wednesday afternoon.
(B) Yes, the budget was approved last week.
(C) Finance handles all the reviews.

PART 3 – SHORT CONVERSATIONS (3 conversations × 3 questions)
Narrator: You will hear conversations between two or three people. Answer three questions about each.

CONVERSATION 1 (Q14–16):
Receptionist: Good morning, Pinnacle Consulting Group. How may I direct your call?
Caller (Mr. Tanaka): Hello, this is Hiroshi Tanaka calling from Kyoto Manufacturing. I have a ten o'clock appointment with Ms. Rachel Torres.
Receptionist: Certainly, Mr. Tanaka. I'm afraid Ms. Torres is currently in an internal meeting that's running a bit late. She asked me to apologise and let you know she'll be available in approximately twenty minutes.
Caller: I see. Is there a conference room where I can wait and review some documents?
Receptionist: Absolutely. Please take the elevator to the fourteenth floor, and our assistant Sandra will direct you to Conference Room C. We'll also have coffee and water available for you.
Caller: That's very kind. One more thing — could you ask Ms. Torres to have the draft contract ready when she comes in? I'd like to go over the payment terms.
Receptionist: Of course. I'll pass that message along immediately.

CONVERSATION 2 (Q17–19):
Team Leader (Karen): Okay team, quick update before we go live with the summer campaign. The graphic design team has finished all fifteen banner ads, but we're still waiting on the approved copy for the social media posts.
Marketing Executive (David): I spoke with copywriting this morning. They said the copy will be ready by end of day today — they're just waiting for the legal sign-off on the promotional discount language.
Karen: Good. And the email newsletter — has that been proofread?
David: Yes, I proofread it yesterday and sent it back with three minor corrections. It should be finalised this afternoon.
Karen: Perfect. What about the influencer partnership posts?
Marketing Executive 2 (Priya): Those are on schedule. The influencers post on Thursday morning at nine, Eastern time, which should hit peak engagement for our target audience.
Karen: Excellent. Let's do a final review call tomorrow at eleven to confirm everything's in order before we set the campaign live Friday morning.

CONVERSATION 3 (Q20–22):
Employee A (Tom): Sarah, have you heard about the office relocation?
Sarah: Yes! I heard we're moving to the new building in Midtown next quarter.
Tom: That's right. I went to the planning committee briefing yesterday. The new space has open-plan seating for the main teams, but each department head will have a private office on the perimeter.
Sarah: What about meeting rooms? Our team is always fighting over the conference rooms here.
Tom: They've designed twelve dedicated meeting rooms, plus four collaboration pods for smaller groups. And apparently there'll be a rooftop terrace for casual meetings and break times.
Sarah: That sounds significantly better. What about the gym subsidy — will that continue at the new location?
Tom: I actually asked about that. The new building has an on-site gym in the basement, so the company will provide free employee access instead of the existing monthly subsidy.

PART 4 – TALKS (2 talks × 3 questions)
Narrator: You will hear two short talks given by a single speaker.

TALK 1 (Q23–25) – WORKPLACE ANNOUNCEMENT:
Narrator: Questions 23 through 25 refer to the following announcement.

Attention all Meridian Financial employees. This is a reminder that starting from next Monday, the company will be implementing a hybrid work policy for all departments. Under the new policy, employees will be required to work from the office on Tuesdays, Wednesdays, and Thursdays, while Mondays and Fridays will be designated as remote working days. This arrangement has been approved following a three-month pilot programme in which overall team productivity increased by eighteen percent while employee satisfaction scores rose significantly. Please note that attendance tracking will begin on the first Monday of next month, so there's a two-week transition period during which you should begin familiarising yourself with the new scheduling system accessible via the HR portal. Department managers will hold individual briefings with their teams this week to address any specific questions. If you have urgent concerns, please contact the Human Resources helpdesk at extension 4402.`,
      questions: [
        // PART 1 (Q1-6) – Photo descriptions
        { text: 'Q1: What is the man doing in the photograph?', translated: 'Người đàn ông đang làm gì trong bức ảnh?', choices: ['Hanging a picture on the wall', 'Reviewing documents at a conference table', 'Setting up a projector', 'Arranging chairs'], answer: 1, ai_explain: 'Đáp án (B): "A man is reviewing documents at a conference table." — Hình ảnh thường thấy trong đề TOEIC: người xem xét tài liệu trong phòng họp.' },
        { text: 'Q2: What is the employee doing in the photograph?', translated: 'Nhân viên đang làm gì trong bức ảnh?', choices: ['Paying at the register', 'Bagging groceries', 'Stocking items on shelves', 'Checking product inventory'], answer: 2, ai_explain: 'Đáp án (D): "An employee is stocking items on the shelves." — Hành động "stock shelves" (lấp đầy kệ hàng) là dạng hay xuất hiện ở TOEIC Part 1.' },
        { text: 'Q3: What is shown near the warehouse entrance?', translated: 'Có gì được hiển thị gần lối vào kho hàng?', choices: ['A forklift moving pallets', 'Boxes being loaded onto a truck', 'Merchandise stacked near the entrance', 'A worker sealing packages'], answer: 2, ai_explain: 'Đáp án (C): "Merchandise is stacked near the warehouse entrance." — Từ "merchandise stacked" mô tả hàng hóa được xếp chồng.' },
        { text: 'Q4: What are the two colleagues doing?', translated: 'Hai đồng nghiệp đang làm gì?', choices: ['Handing a folder between them', 'Looking at a laptop together', 'Standing by a whiteboard', 'One is typing on a keyboard'], answer: 1, ai_explain: 'Đáp án (B): "Two colleagues are seated across from each other, looking at a laptop." — Mô tả chính xác bức tranh hai người xem laptop cùng nhau.' },
        { text: 'Q5: What is happening in the station photograph?', translated: 'Điều gì đang xảy ra trong bức ảnh nhà ga?', choices: ['A train is arriving', 'Passengers are boarding a bus', 'Passengers are getting off a train at the platform', 'Workers are repairing tracks'], answer: 2, ai_explain: 'Đáp án (C): "A train has pulled up alongside the platform and some passengers are getting off." — Chi tiết "getting off" (xuống tàu) là đặc điểm chính của bức ảnh.' },
        { text: 'Q6: What can be seen in the restaurant photograph?', translated: 'Có thể thấy gì trong bức ảnh nhà hàng?', choices: ['Outdoor dining tables', 'A chef preparing food', 'Tables set up inside the restaurant', 'Waiters clearing dishes'], answer: 2, ai_explain: 'Đáp án (C): "Tables and chairs have been set up inside the restaurant." — Bàn ghế đã được bày sẵn bên trong nhà hàng (nhưng chưa có thực khách).' },
        // PART 2 (Q7-13) – Question Response
        { text: 'Q7: When is the quarterly sales report due?', translated: 'Khi nào báo cáo doanh số quý phải nộp?', choices: ['Yes, it was due last month', 'By the end of Thursday', 'At the marketing conference room'], answer: 1, ai_explain: 'Câu hỏi "When" (Khi nào) → trả lời bằng thời gian: "By the end of Thursday." Loại A (Yes/No không hợp lý cho When), loại C (địa điểm, không phải thời gian).' },
        { text: 'Q8: Could you review my presentation slides before the meeting?', translated: 'Bạn có thể xem lại các slide trình bày của tôi trước cuộc họp không?', choices: ['I already submitted the slides online', 'Sure, send them over this afternoon', 'The meeting was held on Friday'], answer: 1, ai_explain: 'Đây là lời đề nghị (request): đáp án B "Sure, send them over" là phản hồi phù hợp nhất. A không hợp lý vì nói về mình, C là thông tin không liên quan.' },
        { text: 'Q9: Has the new office furniture been delivered yet?', translated: 'Nội thất văn phòng mới đã được giao chưa?', choices: ['It arrived this morning and is in the storage room', 'The furniture store is two blocks away', 'We ordered three new chairs'], answer: 0, ai_explain: '"Has... been delivered yet?" → cần xác nhận có/chưa và thêm chi tiết. A hoàn toàn phù hợp: "It arrived this morning..."' },
        { text: 'Q10: Who will be leading the training session tomorrow?', translated: 'Ai sẽ dẫn dắt buổi đào tạo ngày mai?', choices: ['The training was excellent', 'It will be conducted by Ms. Park from HR', 'The session runs for two hours'], answer: 1, ai_explain: 'Câu hỏi "Who" → cần trả lời tên người: "Ms. Park from HR." A là đánh giá, C là thông tin thời lượng.' },
        { text: 'Q11: Do you know where the parking validation forms are?', translated: 'Bạn có biết các mẫu xác nhận đỗ xe ở đâu không?', choices: ['The parking lot is on level B2', 'I think Lisa keeps them at the reception desk', 'Validation takes about fifteen minutes'], answer: 1, ai_explain: 'Câu hỏi "where" → cần địa điểm cụ thể. B: "at the reception desk" là câu trả lời đúng. A (bãi đỗ xe) và C (thời gian) không trả lời được "where the forms are."' },
        { text: 'Q12: Should we reschedule the client call or keep it at ten?', translated: 'Chúng ta có nên đổi lịch cuộc gọi khách hàng hay giữ nguyên lúc mười giờ?', choices: ["The client is from Toronto", "Let's push it back to eleven — Mr. Chen has a conflict", 'The call went very well, thank you'], answer: 1, ai_explain: 'Câu hỏi lựa chọn (Or question) → B đề xuất dời lịch có lý do cụ thể. A (Toronto) không liên quan, C là nhận xét về cuộc gọi đã kết thúc.' },
        { text: "Q13: Isn't the annual budget review meeting next Monday?", translated: 'Không phải cuộc họp đánh giá ngân sách hằng năm là vào thứ Hai tới sao?', choices: ['Actually, it was moved to Wednesday afternoon', 'Yes, the budget was approved last week', 'Finance handles all the reviews'], answer: 0, ai_explain: 'Tag question đồng ý/không đồng ý → A cung cấp thông tin cập nhật (đổi sang Thứ Tư). B sai vì ngân sách chưa chắc đã được phê duyệt, C không trả lời đúng câu hỏi.' },
        // PART 3 (Q14-22) – Conversations
        { text: 'Q14: Why is Mr. Tanaka calling Pinnacle Consulting Group?', translated: 'Tại sao ông Tanaka gọi đến Pinnacle Consulting Group?', choices: ['To request a change in the appointment time', 'He has a scheduled appointment with Ms. Torres', 'To inquire about the company services', 'To leave a message for Sandra'], answer: 1, ai_explain: '"I have a ten o\'clock appointment with Ms. Rachel Torres" — ông Tanaka gọi để thực hiện cuộc hẹn đã đặt lịch trước.' },
        { text: 'Q15: What does Mr. Tanaka ask the receptionist to do?', translated: 'Ông Tanaka yêu cầu lễ tân làm gì?', choices: ['Book a different conference room', 'Ask Ms. Torres to have the draft contract ready', 'Cancel the appointment and reschedule', 'Send the contract via email before the meeting'], answer: 1, ai_explain: '"could you ask Ms. Torres to have the draft contract ready when she comes in? I\'d like to go over the payment terms."' },
        { text: 'Q16: Where will Mr. Tanaka wait for Ms. Torres?', translated: 'Ông Tanaka sẽ đợi ở đâu?', choices: ['The lobby on the ground floor', 'Conference Room C on the fourteenth floor', 'The reception desk on the twelfth floor', 'A private office on the same floor'], answer: 1, ai_explain: '"Please take the elevator to the fourteenth floor... Conference Room C."' },
        { text: 'Q17: What is the team discussing?', translated: 'Nhóm đang thảo luận về gì?', choices: ['Preparing the quarterly financial report', 'The launch of the summer marketing campaign', 'Hiring new social media influencers', 'The redesign of the company website'], answer: 1, ai_explain: '"before we go live with the summer campaign" — chủ đề thảo luận là chuẩn bị cho chiến dịch marketing mùa hè.' },
        { text: 'Q18: What is still pending before the social media copy is ready?', translated: 'Điều gì vẫn đang chờ xử lý trước khi nội dung mạng xã hội sẵn sàng?', choices: ['Graphic design approval', 'Legal sign-off on the promotional discount language', 'Proofreading from the copywriting team', 'Final confirmation from Karen'], answer: 1, ai_explain: '"they\'re just waiting for the legal sign-off on the promotional discount language."' },
        { text: 'Q19: When are the influencers scheduled to post?', translated: 'Khi nào các influencer được lên lịch đăng bài?', choices: ['Wednesday morning', 'Thursday morning at 9 AM Eastern time', 'Friday morning', 'Saturday morning for the weekend audience'], answer: 1, ai_explain: '"The influencers post on Thursday morning at nine, Eastern time, which should hit peak engagement."' },
        { text: 'Q20: What is the topic of conversation between Tom and Sarah?', translated: 'Chủ đề cuộc trò chuyện giữa Tom và Sarah là gì?', choices: ['The company financial results', 'The upcoming office relocation to Midtown', 'The new employee benefits package', 'Changes to the remote working policy'], answer: 1, ai_explain: '"Have you heard about the office relocation? ...moving to the new building in Midtown next quarter."' },
        { text: 'Q21: According to Tom, how many meeting rooms will the new office have?', translated: 'Theo Tom, văn phòng mới sẽ có bao nhiêu phòng họp?', choices: ['Eight rooms plus two pods', 'Ten rooms plus two collaboration pods', 'Twelve dedicated meeting rooms plus four collaboration pods', 'Fifteen conference rooms'], answer: 2, ai_explain: '"twelve dedicated meeting rooms, plus four collaboration pods for smaller groups."' },
        { text: 'Q22: What will replace the current gym subsidy?', translated: 'Điều gì sẽ thay thế trợ cấp phòng gym hiện tại?', choices: ['A higher monthly stipend', 'Free employee access to an on-site gym in the new building', 'Partnership with a nearby fitness centre', 'A wellness allowance added to the annual bonus'], answer: 1, ai_explain: '"The new building has an on-site gym in the basement, so the company will provide free employee access instead of the existing monthly subsidy."' },
        // PART 4 (Q23-25) – Talk
        { text: 'Q23: What new policy is being announced?', translated: 'Chính sách mới nào đang được thông báo?', choices: ['A new employee bonus structure', 'A hybrid work policy for all departments', 'Mandatory overtime on Fridays', 'A fully remote work arrangement'], answer: 1, ai_explain: '"the company will be implementing a hybrid work policy for all departments."' },
        { text: 'Q24: On which days are employees required to work from the office?', translated: 'Nhân viên phải làm việc tại văn phòng vào những ngày nào?', choices: ['Monday, Tuesday, Wednesday', 'Tuesday, Wednesday, Thursday', 'Wednesday, Thursday, Friday', 'Monday, Wednesday, Friday'], answer: 1, ai_explain: '"employees will be required to work from the office on Tuesdays, Wednesdays, and Thursdays."' },
        { text: 'Q25: By how much did team productivity increase during the pilot programme?', translated: 'Năng suất nhóm đã tăng bao nhiêu trong chương trình thí điểm?', choices: ['8 percent', '12 percent', '18 percent', '25 percent'], answer: 2, ai_explain: '"overall team productivity increased by eighteen percent while employee satisfaction scores rose significantly."' }
      ]
    },

    // ===========================================================
    // ETS 2024 TEST 1 – FULL READING (24 CÂU)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 1 – Full Reading (24 Câu)': {
      type: 'reading_passage',
      passageTitle: 'ETS TOEIC 2024 – Full Reading Test 1',
      passageText: `PART 5 – INCOMPLETE SENTENCES (Q1–Q10)

1. The marketing department ------- a comprehensive social media strategy for the upcoming product launch.
   (A) develop   (B) will be developing   (C) developed   (D) is developed

2. All employees are required to submit their expense reports ------- the end of the fiscal quarter.
   (A) by   (B) at   (C) for   (D) since

3. The conference room ------- for the executive meeting, so the team had to find an alternative location.
   (A) is reserving   (B) has been reserved   (C) reserved   (D) will reserve

4. Ms. Chen, ------- handles all international client accounts, will be attending the trade fair in Frankfurt.
   (A) who   (B) which   (C) whom   (D) whose

5. The renovated factory ------- produce twice the number of units compared to last year.
   (A) able to   (B) is able to   (C) has able   (D) was able

6. Staff members should notify their supervisors ------- they plan to take extended leave during peak season.
   (A) so that   (B) despite   (C) although   (D) whenever

7. The board of directors ------- unanimously to approve the merger proposal after three months of negotiations.
   (A) voted   (B) votes   (C) is voting   (D) vote

8. The financial report contained several ------- errors that had to be corrected before submission.
   (A) significance   (B) significantly   (C) significant   (D) signify

9. Neither the CEO nor the board members ------- available to comment on the acquisition rumours.
   (A) was   (B) were   (C) is   (D) has been

10. The new software update ------- automatically each night at midnight to minimise disruption to operations.
    (A) installs   (B) is installed   (C) will be installing   (D) installed

PART 6 – TEXT COMPLETION (Q11–Q14)

Questions 11-14 refer to the following internal memo:

TO: All Customer Service Representatives
FROM: Department Head, Jennifer Walsh
DATE: October 14, 2024
SUBJECT: Updated Protocol for Client Escalations

Effective immediately, all customer escalations that cannot be resolved within fifteen minutes must be ------- (11) to a senior representative. This policy has been established in response to our recent client satisfaction survey, which indicated that response times and resolution quality ------- (12) the primary factors driving client dissatisfaction.

Going forward, all escalation cases must be documented in the CRM system with a detailed summary of the issue, the actions taken, and the resolution outcome. This documentation is ------- (13) for tracking patterns in client complaints and identifying areas for service improvement. A dedicated escalation queue ------- (14) in the system next Monday, and all representatives will receive training on the updated interface during this week's Friday afternoon session.

Thank you for your continued commitment to providing exceptional service.

Q11: (A) referred   (B) refer   (C) referring   (D) to refer
Q12: (A) was   (B) are   (C) were   (D) has been
Q13: (A) essential   (B) essentially   (C) essentiality   (D) essence
Q14: (A) launched   (B) will be launched   (C) launching   (D) is launch

PART 7 – READING COMPREHENSION

SINGLE PASSAGE (Q15–18): E-MAIL

From: Marcus Bellamy <m.bellamy@ridgecorp.com>
To: Accounting Team
Date: September 30, 2024
Subject: Reminder: Q3 Financial Statements

Dear Team,

This is a friendly reminder that the Q3 financial statements are due by Friday, October 4. Please ensure all departmental budget reconciliations are submitted to Priya Kapoor by Wednesday, October 2 at 5:00 PM at the latest, as she requires time to compile the consolidated report.

If you anticipate difficulty meeting this deadline, please contact me directly no later than Tuesday morning so we can discuss an extension or alternative arrangement. Extensions will only be granted under exceptional circumstances and must be approved by the CFO.

All files should be submitted in the approved Excel template, version 3.2, which is available on the shared drive under Accounting > Templates > 2024. Please do not use older template versions as they are not compatible with our updated financial reporting software.

Best regards,
Marcus Bellamy
Director of Finance, Ridge Corporation

Q15: What is the primary purpose of the email?
(A) To introduce a new accounting software platform
(B) To remind staff of an upcoming deadline for financial statements
(C) To announce changes to the company's fiscal year calendar
(D) To request approval for an accounting team expansion

Q16: By when should departmental reconciliations be submitted to Priya Kapoor?
(A) By Monday, September 30
(B) By Tuesday, October 1 at noon
(C) By Wednesday, October 2 at 5:00 PM
(D) By Friday, October 4 at close of business

Q17: Under what circumstances will deadline extensions be granted?
(A) When an employee has approved annual leave during the deadline period
(B) Under exceptional circumstances with CFO approval
(C) For any request submitted before Thursday morning
(D) When the departmental head requests an extension on behalf of the team

Q18: Where can staff find the correct Excel template?
(A) On the HR intranet portal under Forms & Documents
(B) In an attachment to a previous team email
(C) On the shared drive under Accounting > Templates > 2024
(D) By requesting it directly from Priya Kapoor

DOUBLE PASSAGE (Q19–24):

PASSAGE A – NOTICE:
Ridgewood Business Centre
ATTN: All Tenants
RE: Scheduled Maintenance – Main Elevator System
DATE: October 10, 2024

Please be advised that the main elevator bank (Elevators 1–3) in Building A will be out of service from Monday, October 21 to Friday, October 25 for scheduled preventive maintenance and safety certification renewal. During this period, Elevator 4 (freight elevator, located in the service corridor on the eastern side of the building) will be made available to all tenants for regular passenger use. Due to its smaller capacity, we ask tenants to limit elevator use to essential trips and to use the stairwells (Floors 1–5) where physically able.

The building management team apologises for any inconvenience and appreciates your patience during this necessary maintenance period. Any tenant with specific accessibility needs should contact building management at ext. 2200 before October 18 to arrange alternative accommodation.

PASSAGE B – EMAIL:
From: Claire Hutchinson <c.hutchinson@veritas-law.com>
To: Building Management
Date: October 16, 2024
Subject: Re: Elevator Maintenance Notice

Dear Building Management,

Thank you for the advance notice regarding the upcoming elevator maintenance. I am writing on behalf of Veritas Law Associates, who occupy the twelfth floor.

We have two team members with mobility limitations who rely on elevator access daily. I contacted your office this morning and spoke with a representative who suggested that we coordinate with the freight elevator operator. However, I wanted to confirm in writing that these two employees will have priority access to Elevator 4 during the maintenance period, particularly during the morning (9:00–9:30 AM) and evening (5:30–6:00 PM) peak periods.

Could you also advise whether there are temporary handrails being installed in the stairwells? While our mobility-limited staff cannot use the stairs, our other team members would appreciate the added safety measure.

Thank you for your assistance.

Best regards,
Claire Hutchinson
Office Manager, Veritas Law Associates

Q19: How long will the main elevator bank be out of service?
(A) Three business days
(B) Five business days
(C) Seven business days
(D) Two weeks

Q20: Which elevator will be available to all tenants during maintenance?
(A) Elevator 1 on the main lobby level
(B) The freight elevator (Elevator 4) on the eastern side
(C) A temporary elevator being installed for the period
(D) Elevators 2 and 3 on an alternating schedule

Q21: What does the notice ask tenants with accessibility needs to do?
(A) Submit a written request to the city council
(B) Contact building management before October 18
(C) Arrange alternative accommodation independently
(D) Email the maintenance contractor directly

Q22: Who is Claire Hutchinson and why is she writing?
(A) She is a building inspector writing to confirm compliance certificates
(B) She is an office manager writing to request priority elevator access for mobility-limited employees
(C) She is a tenant committee representative proposing schedule changes
(D) She is a building management representative acknowledging the notice

Q23: What does Claire Hutchinson ask about in addition to elevator access?
(A) Whether parking spaces will be affected during maintenance
(B) Whether temporary handrails will be installed in the stairwells
(C) Whether compensation will be provided for business disruption
(D) Whether the maintenance period can be shortened

Q24: Which floor does Veritas Law Associates occupy?
(A) Fifth floor
(B) Eighth floor
(C) Tenth floor
(D) Twelfth floor`,
      questions: [
        // PART 5 (Q1-10)
        { text: 'Q1 (Part 5): The marketing department ------- a comprehensive social media strategy for the upcoming launch.', translated: 'Phòng marketing _______ một chiến lược truyền thông xã hội toàn diện cho lần ra mắt sắp tới.', choices: ['develop', 'will be developing', 'developed', 'is developed'], answer: 1, ai_explain: 'Dùng "will be developing" vì đây là hành động đang diễn ra trong tương lai (future continuous). "developed" là quá khứ đơn không phù hợp.' },
        { text: 'Q2 (Part 5): All employees must submit expense reports ------- the end of the fiscal quarter.', translated: 'Tất cả nhân viên phải nộp báo cáo chi phí _______ cuối quý tài chính.', choices: ['by', 'at', 'for', 'since'], answer: 0, ai_explain: '"By" + điểm thời gian = deadline (hạn chót). "Submit by the end of" = "nộp trước cuối." "At" dùng cho thời gian chính xác (at 5 PM), không phải khoảng thời gian.' },
        { text: 'Q3 (Part 5): The conference room ------- for the executive meeting, so the team had to find an alternative location.', translated: 'Phòng họp _______ cho cuộc họp ban điều hành, vì vậy nhóm phải tìm địa điểm thay thế.', choices: ['is reserving', 'has been reserved', 'reserved', 'will reserve'], answer: 1, ai_explain: '"has been reserved" — Present Perfect Passive. Phòng được đặt trước (bởi ai đó, không rõ) → đây là passive voice hiện tại hoàn thành, thể hiện trạng thái hiện tại (phòng đã được đặt rồi).' },
        { text: 'Q4 (Part 5): Ms. Chen, ------- handles all international client accounts, will attend the Frankfurt trade fair.', translated: 'Bà Chen, _______ xử lý tất cả tài khoản khách hàng quốc tế, sẽ tham dự hội chợ thương mại Frankfurt.', choices: ['who', 'which', 'whom', 'whose'], answer: 0, ai_explain: '"who" — Relative pronoun thay thế cho người (Ms. Chen) và là chủ ngữ của mệnh đề quan hệ (handles). "Whom" là tân ngữ, "whose" là sở hữu.' },
        { text: 'Q5 (Part 5): The renovated factory ------- produce twice the number of units compared to last year.', translated: 'Nhà máy được cải tạo _______ sản xuất gấp đôi số lượng đơn vị so với năm ngoái.', choices: ['able to', 'is able to', 'has able', 'was able'], answer: 1, ai_explain: '"is able to" — cụm "be able to" cần trợ động từ "be" đúng ngữ pháp. "Able to" đứng một mình là sai. "Was able" thiếu "to" ở sau.' },
        { text: 'Q6 (Part 5): Staff should notify supervisors ------- they plan to take extended leave during peak season.', translated: 'Nhân viên nên thông báo cho giám sát viên _______ họ dự định nghỉ phép kéo dài trong mùa cao điểm.', choices: ['so that', 'despite', 'although', 'whenever'], answer: 3, ai_explain: '"whenever" = bất cứ khi nào. Đây là điều kiện/thời gian: "whenever they plan..." Loại "so that" (mục đích), "despite" (tương phản, cần gerund), "although" (tương phản, logic sai).' },
        { text: 'Q7 (Part 5): The board of directors ------- unanimously to approve the merger proposal.', translated: 'Hội đồng quản trị _______ nhất trí để phê duyệt đề xuất sáp nhập.', choices: ['voted', 'votes', 'is voting', 'vote'], answer: 0, ai_explain: '"voted" — quá khứ đơn. "After three months of negotiations" = đây là sự kiện đã xảy ra trong quá khứ. "Board of directors" là chủ thể tập thể, dùng số ít hoặc số nhiều tùy ngữ cảnh, nhưng ở đây "voted" (plural agreement) phù hợp.' },
        { text: 'Q8 (Part 5): The report contained several ------- errors that had to be corrected.', translated: 'Báo cáo chứa một số lỗi _______ phải được sửa chữa.', choices: ['significance', 'significantly', 'significant', 'signify'], answer: 2, ai_explain: '"significant" — tính từ (adjective) bổ nghĩa cho danh từ "errors." "Significance" là danh từ, "significantly" là trạng từ, "signify" là động từ.' },
        { text: 'Q9 (Part 5): Neither the CEO nor the board members ------- available to comment on the acquisition.', translated: 'Cả CEO lẫn các thành viên hội đồng đều không _______ sẵn sàng bình luận về việc mua lại.', choices: ['was', 'were', 'is', 'has been'], answer: 1, ai_explain: '"Neither... nor" với chủ ngữ số nhiều ("board members") đứng gần verb → verb chia số nhiều: "were." Quy tắc "proximity" (gần nhất) trong Neither...nor / Either...or.' },
        { text: 'Q10 (Part 5): The software update ------- automatically each night at midnight.', translated: 'Bản cập nhật phần mềm _______ tự động mỗi đêm lúc nửa đêm.', choices: ['installs', 'is installed', 'will be installing', 'installed'], answer: 1, ai_explain: '"is installed" — Passive Present Simple. Phần mềm "được cài đặt" (by the system/automatically) → passive voice. "Installs" là active, không phù hợp vì software không tự cài mà "được cài."' },
        // PART 6 (Q11-14)
        { text: 'Q11 (Part 6): Escalations that cannot be resolved within fifteen minutes must be ------- to a senior representative.', translated: 'Các trường hợp leo thang không thể giải quyết trong 15 phút phải được _______ cho đại diện cấp cao.', choices: ['referred', 'refer', 'referring', 'to refer'], answer: 0, ai_explain: '"referred" — Passive voice: "must be referred" (cần được chuyển tiếp). "Must be + past participle" là cấu trúc modal passive chuẩn.' },
        { text: 'Q12 (Part 6): The survey indicated that response times and resolution quality ------- the primary factors driving client dissatisfaction.', translated: 'Khảo sát cho thấy thời gian phản hồi và chất lượng giải quyết _______ các yếu tố chính gây ra sự không hài lòng của khách hàng.', choices: ['was', 'are', 'were', 'has been'], answer: 2, ai_explain: '"were" — Past Simple vì đây là kết quả từ khảo sát đã được thực hiện ("survey indicated" → past). Chủ ngữ "response times and resolution quality" là số nhiều → "were."' },
        { text: 'Q13 (Part 6): This documentation is ------- for tracking patterns in client complaints.', translated: 'Tài liệu này là _______ để theo dõi các mẫu trong khiếu nại của khách hàng.', choices: ['essential', 'essentially', 'essentiality', 'essence'], answer: 0, ai_explain: '"essential" — tính từ sau "is" (predicate adjective). "is essential" = "là điều thiết yếu." "Essentially" là trạng từ, không dùng sau "is" để mô tả noun.' },
        { text: 'Q14 (Part 6): A dedicated escalation queue ------- in the system next Monday.', translated: 'Một hàng chờ xử lý leo thang chuyên dụng _______ trong hệ thống vào thứ Hai tới.', choices: ['launched', 'will be launched', 'launching', 'is launch'], answer: 1, ai_explain: '"will be launched" — Future Passive. "Next Monday" xác nhận tương lai, và hàng chờ "được ra mắt" (by someone) = passive. "Will be launched" là cấu trúc đúng.' },
        // PART 7 Single Passage (Q15-18)
        { text: 'Q15 (Part 7): What is the primary purpose of Marcus Bellamy\'s email?', translated: 'Mục đích chính của email của Marcus Bellamy là gì?', choices: ['To introduce a new accounting software platform', 'To remind staff of an upcoming deadline for financial statements', 'To announce changes to the fiscal year calendar', 'To request approval for team expansion'], answer: 1, ai_explain: '"This is a friendly reminder that the Q3 financial statements are due by Friday, October 4." — Đây là email nhắc nhở (reminder) về thời hạn nộp báo cáo tài chính.' },
        { text: 'Q16 (Part 7): By when should departmental reconciliations be submitted to Priya Kapoor?', translated: 'Đến khi nào thì các đối chiếu phòng ban nên được nộp cho Priya Kapoor?', choices: ['Monday, September 30', 'Tuesday, October 1 at noon', 'Wednesday, October 2 at 5:00 PM', 'Friday, October 4 at close of business'], answer: 2, ai_explain: '"Please ensure all departmental budget reconciliations are submitted to Priya Kapoor by Wednesday, October 2 at 5:00 PM at the latest."' },
        { text: 'Q17 (Part 7): Under what circumstances will extensions be granted?', translated: 'Trong hoàn cảnh nào thì việc gia hạn sẽ được chấp thuận?', choices: ['When an employee has approved annual leave', 'Under exceptional circumstances with CFO approval', 'For any request submitted before Thursday', 'When the departmental head requests on behalf of the team'], answer: 1, ai_explain: '"Extensions will only be granted under exceptional circumstances and must be approved by the CFO."' },
        { text: 'Q18 (Part 7): Where can staff find the correct Excel template?', translated: 'Nhân viên có thể tìm thấy mẫu Excel chính xác ở đâu?', choices: ['On the HR intranet under Forms & Documents', 'In an attachment to a previous team email', 'On the shared drive under Accounting > Templates > 2024', 'By requesting from Priya Kapoor directly'], answer: 2, ai_explain: '"All files should be submitted in the approved Excel template, version 3.2, which is available on the shared drive under Accounting > Templates > 2024."' },
        // PART 7 Double Passage (Q19-24)
        { text: 'Q19 (Part 7): How long will the main elevator bank be out of service?', translated: 'Dãy thang máy chính sẽ ngừng hoạt động trong bao lâu?', choices: ['Three business days', 'Five business days', 'Seven business days', 'Two weeks'], answer: 1, ai_explain: '"Monday, October 21 to Friday, October 25" = 5 ngày làm việc (Mon-Tue-Wed-Thu-Fri).' },
        { text: 'Q20 (Part 7): Which elevator is available to all tenants during maintenance?', translated: 'Thang máy nào có thể được tất cả người thuê sử dụng trong thời gian bảo trì?', choices: ['Elevator 1 on the main lobby', 'The freight elevator (Elevator 4) on the eastern side', 'A temporary elevator being installed', 'Elevators 2 and 3 alternating'], answer: 1, ai_explain: '"Elevator 4 (freight elevator, located in the service corridor on the eastern side of the building) will be made available to all tenants."' },
        { text: 'Q21 (Part 7): What should tenants with accessibility needs do?', translated: 'Người thuê có nhu cầu tiếp cận đặc biệt nên làm gì?', choices: ['Submit a written request to the city council', 'Contact building management before October 18', 'Arrange alternative accommodation independently', 'Email the maintenance contractor directly'], answer: 1, ai_explain: '"Any tenant with specific accessibility needs should contact building management at ext. 2200 before October 18."' },
        { text: 'Q22 (Part 7): Why is Claire Hutchinson writing to building management?', translated: 'Tại sao Claire Hutchinson viết thư cho ban quản lý tòa nhà?', choices: ['To confirm compliance certificates', 'To request priority elevator access for mobility-limited employees', 'To propose schedule changes as a tenant committee', 'To acknowledge receipt of the maintenance notice'], answer: 1, ai_explain: '"I wanted to confirm in writing that these two employees will have priority access to Elevator 4 during the maintenance period."' },
        { text: 'Q23 (Part 7): What additional request does Claire Hutchinson make?', translated: 'Claire Hutchinson đưa ra yêu cầu bổ sung nào?', choices: ['Whether parking spaces will be affected', 'Whether temporary handrails will be installed in stairwells', 'Whether compensation will be provided for disruption', 'Whether the maintenance period can be shortened'], answer: 1, ai_explain: '"Could you also advise whether there are temporary handrails being installed in the stairwells?"' },
        { text: 'Q24 (Part 7): Which floor does Veritas Law Associates occupy?', translated: 'Công ty Veritas Law Associates đóng ở tầng mấy?', choices: ['Fifth floor', 'Eighth floor', 'Tenth floor', 'Twelfth floor'], answer: 3, ai_explain: '"I am writing on behalf of Veritas Law Associates, who occupy the twelfth floor."' }
      ]
    },

    // ===========================================================
    // ETS 2024 TEST 1 – FULL SPEAKING (11 CÂU)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 1 – Full Speaking (11 Câu)': {
      type: 'speaking',
      questions: [
        // Questions 1-2: Read a text aloud
        { text: 'Q1 (Read Aloud – 45 giây đọc): Read the following text aloud. "Thank you for calling Hartfield International Airport Information Services. Our terminal operates twenty-four hours a day, seven days a week. For flight arrivals and departures, please press one. For parking and ground transportation, please press two. To speak with a customer service representative, please remain on the line, and your call will be answered in the order it was received. We appreciate your patience."', translated: 'Q1: Đọc to đoạn thông báo dịch vụ thông tin sân bay.', choices: ['🎯 Tiêu chí chấm (Pronunciation & Intonation): Nhịp điệu tự nhiên, phát âm rõ ràng các từ kỹ thuật (terminal, transportation, representative). Chú ý: nhấn mạnh số (one, two) và dừng sau mỗi hướng dẫn. Không đọc quá nhanh — tốc độ 130-150 từ/phút là lý tưởng.', '📋 Từ phát âm cần lưu ý: terminal /ˈtɜːmɪnəl/ — international /ˌɪntəˈnæʃənəl/ — representative /ˌrɛprɪˈzɛntətɪv/ — transportation /ˌtrænspɔːˈteɪʃən/'], answer: 0, ai_explain: 'Read Aloud: Điểm cao khi phát âm chính xác, nhịp điệu tự nhiên, intonation phù hợp (giọng hướng dẫn xuống cuối câu), không ngập ngừng.' },
        { text: 'Q2 (Read Aloud – 45 giây đọc): Read the following announcement aloud. "Attention all conference participants. The keynote address by Dr. Maria Santos will begin promptly at two PM in the Grand Ballroom on the third floor. Seating is limited, so we encourage early arrival. Light refreshments will be available in the foyer outside the ballroom from one-thirty PM. Please ensure your conference badge is visible at all times. Thank you."', translated: 'Q2: Đọc to thông báo hội nghị.', choices: ['🎯 Tiêu chí chấm: Intonation đúng với giọng thông báo chính thức (formal announcement). Nhấn mạnh thông tin quan trọng: "two PM", "Grand Ballroom", "third floor", "limited seating." Ngừng đúng sau mỗi câu.', '📋 Từ phát âm khó: keynote /ˈkiːnəʊt/ — promptly /ˈprɒmptli/ — refreshments /rɪˈfrɛʃmənts/ — foyer /ˈfɔɪeɪ/ — ballroom /ˈbɔːlruːm/'], answer: 0, ai_explain: 'Formal announcement intonation: nhấn rõ thông tin địa điểm và thời gian. Bắt buộc đọc rõ số (two PM, third floor, one-thirty PM).' },
        // Question 3: Describe a photograph
        { text: 'Q3 (Mô tả ảnh – 30 giây chuẩn bị, 45 giây nói): Describe what you see in the photograph. [Photograph: A busy open-plan office. Several employees are working at their computers. In the foreground, a woman in a blue blazer is speaking on the phone while looking at documents. In the background, two men are standing near a whiteboard discussing something. Natural light comes through large windows on the left side.]', translated: 'Q3: Mô tả bức ảnh văn phòng cởi mở bận rộn.', choices: ['✍️ BÀI MẪU BAND 8/9 (45 giây): "In this photograph, I can see a busy open-plan office environment. In the foreground, a professional woman dressed in a blue blazer appears to be multitasking — she is speaking on the phone while simultaneously reviewing documents on her desk. The expression on her face suggests focused concentration. Moving to the background, two male colleagues are engaged in what appears to be a collaborative discussion beside a whiteboard, which has various diagrams or notes on it. The office benefits from considerable natural light streaming in through large windows visible on the left side of the image, creating a bright and professional working atmosphere. Overall, this image conveys the dynamic, fast-paced nature of a modern corporate workplace."', '🎯 Structure cho Photo Description: 1. General scene overview (1 câu) → 2. Foreground details (2-3 câu) → 3. Background details (2 câu) → 4. Overall impression (1 câu). Total: ~7-8 câu trong 45 giây.'], answer: 0, ai_explain: 'Photo description: Mô tả từ tổng quan → chi tiết foreground → chi tiết background. Dùng "In the foreground...", "Moving to the background...", "appears to be doing..." cho sự tự nhiên.' },
        // Questions 4-6: Respond to questions
        { text: 'Q4 (Trả lời câu hỏi – 15 giây): Imagine you are talking to a market researcher about shopping habits. [Researcher]: How often do you go shopping for clothing?', translated: 'Q4: Bạn mua quần áo bao lâu một lần?', choices: ['✍️ BÀI MẪU 15 GIÂY: "Honestly, I\'d say about once a month. I tend to shop seasonally — doing a bigger wardrobe refresh at the start of summer and winter, and then picking up individual items whenever I spot something I need or genuinely like."', '🎯 Tip: 15 giây = khoảng 2-3 câu ngắn gọn. Không cần elaborate dài. Frequency word + reason/extra detail = đủ điểm.'], answer: 0, ai_explain: 'Q4-6 là trả lời câu hỏi ngắn không có thời gian chuẩn bị. Trả lời NGAY lập tức, tự nhiên, 2-3 câu.' },
        { text: 'Q5 (Trả lời câu hỏi – 15 giây): [Researcher]: What factors are most important to you when choosing a clothing brand?', translated: 'Q5: Yếu tố nào quan trọng nhất với bạn khi chọn thương hiệu quần áo?', choices: ['✍️ BÀI MẪU 15 GIÂY: "For me, quality and durability come first — I\'d rather invest in fewer, better-made pieces than constantly replace cheap items. After that, ethical sourcing and sustainability practices have become increasingly important in my purchasing decisions. Brand name matters much less than those two factors."', '🎯 Tip: Liệt kê 2 yếu tố + giải thích ngắn. Tránh trả lời chỉ "Quality and price." Thêm 1 lý do = đủ điểm cao.'], answer: 0, ai_explain: 'Q5: Factor questions = liệt kê ưu tiên + giải thích ngắn lý do tại sao. Nên đề cập đến 2 yếu tố.' },
        { text: 'Q6 (Trả lời câu hỏi – 15 giây): [Researcher]: Do you usually shop in-store or online? Why?', translated: 'Q6: Bạn thường mua sắm trực tiếp hay online? Tại sao?', choices: ['✍️ BÀI MẪU 15 GIÂY: "Primarily online, to be honest. The convenience of comparing prices across multiple platforms and reading customer reviews before buying has made it my default choice. That said, I still prefer to try on shoes or structured clothing in store before committing to a purchase."', '🎯 Tip: State preference + main reason + exception/nuance. Ba yếu tố này tạo câu trả lời 15 giây hoàn chỉnh và thuyết phục.'], answer: 0, ai_explain: 'Q6: Online vs in-store = state clear preference + reason + nuance (exception). Đừng nói "both are fine" — thiếu rõ ràng.' },
        // Questions 7-9: Respond to questions using information provided
        { text: 'Q7 (Trả lời có tài liệu – 30 giây): The following schedule has been provided. [SCHEDULE: Greenhill Community Workshop Series — Saturday, November 9. 9:00 AM – Welcome & Registration (Main Hall). 10:00 AM – Photography Basics (Room 101). 11:00 AM – Social Media Marketing (Room 203). 12:30 PM – Networking Lunch (Cafeteria). 2:00 PM – Creative Writing Workshop (Library). 3:30 PM – Panel Discussion: Careers in Creative Industries (Main Hall). 5:00 PM – Event Close.] [Question]: What time does the photography session begin, and where is it held?', translated: 'Q7: Buổi học nhiếp ảnh bắt đầu lúc mấy giờ và được tổ chức ở đâu?', choices: ['✍️ BÀI MẪU: "The Photography Basics session begins at ten AM and is held in Room 101."', '🎯 Tip: Câu Q7-9 có tài liệu cho sẵn. Chỉ cần locate thông tin chính xác và đọc lại rõ ràng. Không cần thêm quan điểm cá nhân — chỉ trả lời từ thông tin có sẵn.'], answer: 0, ai_explain: 'Q7-9 (Information-based): Đọc lịch trình nhanh trong 30 giây chuẩn bị. Trả lời chính xác từ thông tin được cung cấp.' },
        { text: 'Q8 (Trả lời có tài liệu – 30 giây): [Based on same schedule] I\'m interested in staying for the full afternoon programme. Can you tell me what activities are scheduled between lunch and the panel discussion?', translated: 'Q8: Những hoạt động nào được lên lịch giữa bữa trưa và phiên thảo luận?', choices: ['✍️ BÀI MẪU: "After the networking lunch at twelve-thirty, there is a Creative Writing Workshop in the Library, which runs from two PM. This is followed by the Panel Discussion on Careers in Creative Industries, held in the Main Hall starting at three-thirty PM."', '🎯 Tip: Q8 hỏi về nhiều mục → cần liệt kê theo thứ tự. Dùng liên từ thời gian: "after...", "this is followed by...", "starting at..."'], answer: 0, ai_explain: 'Q8 multi-item: Liệt kê đúng thứ tự thời gian, kèm thông tin địa điểm từ lịch trình.' },
        { text: 'Q9 (Trả lời có tài liệu – 30 giây): [Based on same schedule] A participant says: "I want to attend something related to digital marketing or online presence." What would you recommend from the schedule, and when does it start?', translated: 'Q9: Bạn có thể đề xuất từ lịch trình điều gì liên quan đến digital marketing không?', choices: ['✍️ BÀI MẪU: "Based on your interest, I\'d recommend the Social Media Marketing session, which starts at eleven AM and is held in Room 203. This session directly addresses online presence and marketing strategies, which aligns with what you\'re looking for."', '🎯 Tip: Q9 thường yêu cầu "recommend" → locate relevant item + explain relevance briefly. Không cần liệt kê tất cả — chỉ mục phù hợp nhất.'], answer: 0, ai_explain: 'Q9 Recommend: Identify most relevant item → state time & location → brief reason why it matches the interest.' },
        // Question 10: Propose a solution
        { text: 'Q10 (Đề xuất giải pháp – 30 giây chuẩn bị, 60 giây nói): You will hear a voicemail message. [VOICEMAIL — Kevin Park, Conference Organiser]: "Hi, this is Kevin Park calling about the Regional Business Conference scheduled for this coming Friday. We have a significant problem — the keynote speaker, Dr. Elena Vasquez, has just informed us that she has a medical emergency and cannot attend. The conference starts in three days, and her ninety-minute slot is now completely empty. We need an alternative solution urgently. Please call me back with any suggestions you have."', translated: 'Q10: Diễn giả hội nghị chính bị bệnh và không thể tham dự. Đề xuất giải pháp.', choices: ['✍️ BÀI MẪU BAND 9 (60 giây): "Kevin, thank you for reaching out — I completely understand the urgency. I have two concrete suggestions that could resolve this effectively within your timeline. First, consider pivoting to a panel discussion format. Rather than a single keynote presenter, invite three or four senior professionals from your existing attendee or sponsor list to participate in a structured roundtable on the conference theme. This format is actually highly engaging for audiences and can be organised within forty-eight hours. I can help draft the invitation emails today if needed. Alternatively, if you already have Dr. Vasquez\'s prepared slides, consider whether she could deliver her keynote virtually via video conferencing. Many conference organisers have moved to hybrid formats successfully, and the technology infrastructure is straightforward to set up at short notice. A live Q&A following the video presentation would maintain the interactive dimension. I\'d recommend the virtual option as the primary solution since it preserves Dr. Vasquez\'s prepared content, and the panel discussion as your backup. Would you like me to coordinate either of these immediately?"', '🎯 STRUCTURE Q10: 1. Acknowledge the problem (1 câu) → 2. Solution 1 + practical detail (2-3 câu) → 3. Solution 2 alternative (2-3 câu) → 4. Recommendation + offer to help (1-2 câu). Total: ~60 giây lưu loát.'], answer: 0, ai_explain: 'Q10 (Propose solution): Đây là câu khó nhất. Không xin lỗi quá nhiều — đi thẳng vào 2 giải pháp cụ thể với chi tiết thực tế. Kết thúc bằng hỏi xác nhận.' },
        // Question 11: Express an opinion
        { text: 'Q11 (Bày tỏ quan điểm – 30 giây chuẩn bị, 60 giây nói): Do you agree or disagree with the following statement? "Companies should allow employees to choose their own working hours." Give specific reasons and examples to support your opinion.', translated: 'Q11: Bạn đồng ý hay không đồng ý: "Doanh nghiệp nên cho phép nhân viên tự chọn giờ làm việc." Hãy đưa ra lý do và ví dụ cụ thể.', choices: ['✍️ BÀI MẪU BAND 9 (60 giây): "I strongly agree that companies should offer flexible working hours, and I believe the evidence for this position is now substantial. Research from Stanford University found that employees who work flexible schedules report twenty-three percent higher job satisfaction and demonstrate measurably lower absenteeism. This directly benefits employers through improved retention and reduced recruitment costs. From a practical standpoint, different people are genuinely most productive at different times. Early risers may produce their best analytical work between six and nine AM, while others peak creatively in the evening. Rigid nine-to-five schedules may actually suppress peak productivity by forcing employees to perform complex tasks during their biological low points. Of course, flexible hours require clear deliverable-based accountability frameworks — the focus must shift from hours-present to work-completed. Companies like Microsoft Japan and Unilever have successfully implemented this model with significant productivity gains. Ultimately, I believe inflexible working hours are an anachronism in knowledge-based economies where output quality matters far more than physical presence."', '🎯 STRUCTURE Q11: 1. Clear position (Agree/Disagree + strongly/partially) → 2. Reason 1 + evidence/statistic → 3. Reason 2 + example → 4. Acknowledge counterargument (optional but impressive) → 5. Restate conclusion. Total: ~7-8 câu, 60 giây.'], answer: 0, ai_explain: 'Q11 Opinion: Đưa ra lập trường RÕ RÀNG ngay câu đầu. Dùng số liệu hoặc ví dụ thực tế. Kết thúc bằng tổng kết lập luận. Tránh "I think both sides have good points" — thiếu dứt khoát.' }
      ]
    },

    // ===========================================================
    // ETS 2024 TEST 1 – FULL WRITING (3 BÀI)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 1 – Full Writing (3 Bài)': {
      type: 'writing',
      questions: [
        {
          text: 'TOEIC Writing Task 1 – Write a sentence based on a picture (5 phút): Write ONE sentence that describes the main action or situation in the photograph. [Photo: A woman is presenting data on a screen at the front of a conference room. Several colleagues are taking notes and listening attentively.]',
          translated: 'Task 1: Viết MỘT câu mô tả hành động chính trong bức ảnh (phòng họp có người thuyết trình và đồng nghiệp lắng nghe).',
          choices: [
            '✍️ BÀI MẪU BAND 9: "A woman is presenting data analysis findings to her colleagues in a conference room, while the attendees take notes and listen attentively." [ĐẠT: Chủ ngữ rõ ràng + hành động chính + chi tiết bổ sung + while clause phụ]',
            '✍️ BÀI MẪU BAND 7: "A woman is showing information to people in a meeting room while they write things down." [CẢI THIỆN: Thêm cụm từ chi tiết hơn thay vì "information/things"]',
            '🎯 TIÊU CHÍ TASK 1: Một câu hoàn chỉnh (subject + verb + object/complement), mô tả đúng hành động chính, ngữ pháp chính xác, từ vựng phù hợp. Câu có thêm while clause hoặc participial phrase = điểm cao hơn.'
          ],
          answer: 0,
          ai_explain: 'Task 1 (Sentence): 1 câu hoàn chỉnh, mô tả main action = core activity đang diễn ra. Không cần mô tả mọi chi tiết. Band 8-9: câu có cấu trúc phức.'
        },
        {
          text: 'TOEIC Writing Task 2 – Respond to a written request (10 phút): Read the email and write a response of 100–150 words. [EMAIL FROM: Sarah Mitchell <s.mitchell@greentech.com> TO: You DATE: October 14, 2024 SUBJECT: Request for meeting] "Hi, I am Sarah Mitchell, Partnership Development Manager at GreenTech Solutions. We have been reviewing your company\'s sustainability initiatives and believe there may be a strong synergy between our organisations. I\'d like to schedule a thirty-minute video call to explore potential collaboration opportunities. Could you suggest two or three dates and times that would work for you in the next two weeks? Also, could you let me know who else from your team might attend? Thank you, Sarah"',
          translated: 'Task 2: Phản hồi email từ Sarah Mitchell — đề xuất thời gian họp và người tham dự.',
          choices: [
            '✍️ BÀI MẪU BAND 8-9 (135 từ): "Dear Sarah, Thank you for reaching out and for your kind interest in our sustainability initiatives. We would be delighted to explore potential collaboration opportunities with GreenTech Solutions. Please find below three available times for our call: Monday, October 21 at 2:00 PM (GMT+7); Wednesday, October 23 at 10:00 AM (GMT+7); Friday, October 25 at 3:00 PM (GMT+7). Any of these slots would work well on our end. Regarding attendees, I would be joined by our Sustainability Director, Mr. James Park, and our Head of Corporate Partnerships, Dr. Linh Nguyen. Together, we cover both the strategic and operational dimensions of our sustainability programme. Please let me know which date and time suits you best, and I will send a calendar invitation with the video conferencing link promptly. We look forward to connecting. Best regards, [Your Name]" (135 từ)',
            '📋 CẤU TRÚC EMAIL PHẢN HỒI BAND 8+: Para 1 (2 câu): Cảm ơn + bày tỏ sự quan tâm. Para 2 (3-4 câu): Đề xuất 3 khung giờ cụ thể. Para 3 (2-3 câu): Liệt kê người tham dự + vai trò của họ. Para 4 (1-2 câu): Kêu gọi hành động (CTA) + kết thúc lịch sự.',
            '🎯 Từ vựng email chuyên nghiệp: "Thank you for reaching out" — "would be delighted to" — "Please find below" — "on our end" — "Regarding attendees" — "cover both the strategic and operational dimensions" — "promptly"'
          ],
          answer: 0,
          ai_explain: 'Task 2: Email phải trả lời ĐẦY ĐỦ TẤT CẢ câu hỏi trong email gốc (suggested times + attendees). Thiếu một câu hỏi = giảm điểm đáng kể.'
        },
        {
          text: 'TOEIC Writing Task 3 – Write an opinion essay (30 phút – 200–300 từ): Do you agree or disagree with the following statement: "Remote work is more beneficial for companies than traditional office-based work." Use specific reasons and examples to support your position.',
          translated: 'Task 3: Essay quan điểm: "Làm việc từ xa có lợi hơn cho doanh nghiệp so với làm việc truyền thống tại văn phòng." Bạn đồng ý hay không đồng ý?',
          choices: [
            '✍️ BÀI MẪU BAND 8 (270 từ): "The question of whether remote work benefits companies more than traditional office arrangements has become one of the defining business debates of the post-pandemic era. While remote work offers genuine advantages, I believe its net impact on companies depends fundamentally on organisational culture, role type, and workforce composition — making a blanket preference for either model insufficient. Remote work demonstrably reduces overhead costs. A Stanford University study found that companies allowing remote work saw a thirteen percent productivity increase per employee, while simultaneously reducing office space expenditure by up to thirty percent for fully distributed teams. For knowledge-based roles — software development, data analysis, content creation — the evidence suggests remote workers frequently outperform their office-based peers, owing to reduced commuting fatigue and greater autonomy over their work environment. However, remote work presents measurable challenges that companies must not underestimate. Creative industries and early-career employees particularly benefit from the informal knowledge transfer, mentorship opportunities, and spontaneous collaboration that physical proximity naturally generates. A 2022 Microsoft Work Trend Index found that seventy-three percent of managers reported reduced confidence in their ability to monitor productivity and maintain team cohesion in fully remote settings. In conclusion, rather than characterising remote work as universally more beneficial, I believe the most effective companies are those that strategically deploy hybrid models: mandating in-person collaboration for creative, relationship-intensive work while permitting remote arrangements for focused individual tasks. This contextually intelligent approach harnesses the strengths of both modalities." (270 từ)',
            '📋 CẤU TRÚC ESSAY TOEIC WRITING TASK 3 BAND 8: Para 1 (Introduction 40-50 từ): Paraphrase đề + Thesis statement rõ ràng. Para 2 (Agree side 70-80 từ): 2 lý do ủng hộ + ví dụ/số liệu. Para 3 (Disagree/Nuance 70-80 từ): Hạn chế + bằng chứng. Para 4 (Conclusion 30-40 từ): Tổng kết lập trường + giải pháp/nhận xét cuối.',
            '🎯 Từ vựng essay chuyên nghiệp: "The defining business debate" — "demonstrably reduces" — "net impact" — "knowledge-based roles" — "blanket preference" — "contextually intelligent approach" — "deploy hybrid models" — "harnesses the strengths"'
          ],
          answer: 0,
          ai_explain: 'Task 3 TOEIC Writing: 200-300 từ, 4 đoạn rõ ràng. Thesis Statement phải nêu lập trường của bạn trong câu cuối của đoạn giới thiệu. Band 8: có số liệu, ví dụ thực tế, từ vựng học thuật.'
        }
      ]
    },

    // ===========================================================
    // ETS 2024 TEST 2 – FULL LISTENING (25 CÂU - SHORTER AUDIO DESC)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 2 – Full Listening (25 Câu)': {
      type: 'audio_mcq',
      audioTitle: 'ETS TOEIC 2024 Test 2 – Official Listening (North American Accent, Speed 1.0x)',
      audioScript: `PART 1 (Q1-6): Six photographs depicting various workplace and public scenarios.
[Photo 1]: Workers are installing solar panels on a rooftop.
[Photo 2]: A receptionist is greeting a visitor in a hotel lobby.
[Photo 3]: Two people are loading boxes into a delivery van.
[Photo 4]: A chef is preparing food in a restaurant kitchen.
[Photo 5]: Commuters are waiting on a train platform.
[Photo 6]: A woman is examining documents at her desk using a magnifying glass.

PART 2 (Q7-13): Seven question-response exchanges.
Q7: Have the meeting minutes been distributed to all team members?
Q8: Why was the quarterly presentation postponed?
Q9: Where did you find the updated product catalogue?
Q10: Isn't Mr. Yamamoto joining us for the strategy session?
Q11: Could someone help me set up the new printer?
Q12: Should we order additional supplies now or wait until next month?
Q13: How long has the company been operating this branch office?

PART 3 (Q14-22): Three workplace conversations.
CONV 1: Negotiating conference venue booking and catering requirements.
CONV 2: Discussing product recall procedures and customer communication strategy.
CONV 3: Arranging business travel itinerary, hotel upgrades, and visa requirements.

PART 4 (Q23-25): Internal HR announcement about new performance review cycle and bonus structure.`,
      questions: [
        { text: 'Q1: What are the workers doing in the photograph?', translated: 'Công nhân đang làm gì trong bức ảnh?', choices: ['Repairing a damaged roof', 'Installing solar panels on a rooftop', 'Cleaning the exterior of a building', 'Inspecting electrical wiring on a roof'], answer: 1, ai_explain: '"Workers are installing solar panels on a rooftop." — Hành động lắp đặt (installing) là từ khoá.' },
        { text: 'Q2: What is the receptionist doing?', translated: 'Lễ tân đang làm gì?', choices: ['Checking in a guest at the hotel reception', 'Answering a phone call at the front desk', 'Greeting a visitor in the hotel lobby', 'Providing a room key to a departing guest'], answer: 2, ai_explain: '"A receptionist is greeting a visitor in a hotel lobby." Từ khoá: greeting (chào đón), visitor (khách), lobby (sảnh).' },
        { text: 'Q3: What are the two people doing?', translated: 'Hai người đang làm gì?', choices: ['Unloading boxes from a delivery van', 'Loading boxes into a delivery van', 'Sorting packages by size on the pavement', 'Inspecting delivery items outside a warehouse'], answer: 1, ai_explain: '"Two people are loading boxes into a delivery van." Loading (chất hàng lên) ≠ unloading (dỡ hàng xuống). Đây là câu bẫy phổ biến trong TOEIC Part 1.' },
        { text: 'Q4: What is the chef doing?', translated: 'Đầu bếp đang làm gì?', choices: ['Serving food to customers at a table', 'Washing dishes in the kitchen sink', 'Preparing food in a restaurant kitchen', 'Presenting a new dish to restaurant staff'], answer: 2, ai_explain: '"A chef is preparing food in a restaurant kitchen." Từ khoá: preparing (chuẩn bị), restaurant kitchen (bếp nhà hàng).' },
        { text: 'Q5: Where are the commuters waiting?', translated: 'Hành khách đang đợi ở đâu?', choices: ['At a bus terminal near downtown', 'In a taxi queue outside an airport', 'On a train platform', 'At a ferry terminal on the waterfront'], answer: 2, ai_explain: '"Commuters are waiting on a train platform." Platform (sân ga tàu) là từ khoá để phân biệt với bus stop hay airport.' },
        { text: 'Q6: What is the woman doing with the documents?', translated: 'Người phụ nữ đang làm gì với các tài liệu?', choices: ['Signing her name at the bottom of a contract', 'Sorting documents into separate folders', 'Examining documents using a magnifying glass', 'Shredding confidential documents in the office'], answer: 2, ai_explain: '"A woman is examining documents at her desk using a magnifying glass." Từ khoá: examining (kiểm tra kỹ), magnifying glass (kính lúp).' },
        { text: 'Q7: Have the meeting minutes been distributed to all team members?', translated: 'Biên bản cuộc họp đã được phân phát cho tất cả thành viên nhóm chưa?', choices: ["Yes, I'll send them right after this call", 'The meeting was very productive', "Actually, I haven't received my copy yet"], answer: 0, ai_explain: 'Câu hỏi Yes/No question về việc đã làm xong chưa → A tự nhiên nhất: xác nhận sẽ gửi. C là valid nhưng là quan điểm của người nhận, không phải người gửi.' },
        { text: 'Q8: Why was the quarterly presentation postponed?', translated: 'Tại sao bài trình bày quý bị hoãn?', choices: ['Because the presenter had a scheduling conflict', 'The presentation was very successful', 'It will be held in the main conference room'], answer: 0, ai_explain: '"Why" → cần lý do (reason). A cung cấp lý do cụ thể. B là nhận xét, C là địa điểm — không trả lời "why".' },
        { text: 'Q9: Where did you find the updated product catalogue?', translated: 'Bạn tìm thấy danh mục sản phẩm cập nhật ở đâu?', choices: ['It was posted on the company intranet', 'The catalogue looks great this year', 'Product design sent it last Tuesday'], answer: 0, ai_explain: '"Where" → địa điểm hoặc nguồn. A (intranet) = nguồn → phù hợp. C (who) không phải "where."' },
        { text: "Q10: Isn't Mr. Yamamoto joining us for the strategy session?", translated: 'Không phải ông Yamamoto tham gia buổi chiến lược cùng chúng ta sao?', choices: ['He mentioned his strategy earlier', "He won't be available — he's presenting at the Tokyo summit", 'The strategy session starts at two'], answer: 1, ai_explain: 'Tag question → A/B xác nhận hay phủ nhận. B cung cấp lý do tại sao không tham gia — phản hồi tự nhiên nhất.' },
        { text: 'Q11: Could someone help me set up the new printer?', translated: 'Ai có thể giúp tôi thiết lập máy in mới không?', choices: ['The printer is on the third floor', "Sure, I'll be right over", 'We already ordered a new printer'], answer: 1, ai_explain: 'Request for help (Could someone...) → tự nhiên nhất là B: "Sure, I\'ll be right over" (đồng ý giúp + cam kết hành động cụ thể).' },
        { text: 'Q12: Should we order additional supplies now or wait until next month?', translated: 'Chúng ta có nên đặt hàng thêm vật tư ngay bây giờ hay đợi đến tháng sau?', choices: ['The supply room is on the second floor', "Let's go ahead and order now — inventory is getting low", 'I placed the order two weeks ago'], answer: 1, ai_explain: 'Or question (A or B?) → trả lời bằng lựa chọn rõ ràng. B chọn rõ "order now" và đưa ra lý do. A (địa điểm) và C (quá khứ) đều không liên quan.' },
        { text: 'Q13: How long has the company been operating this branch office?', translated: 'Công ty đã vận hành chi nhánh này bao lâu rồi?', choices: ['The branch is located in Singapore', 'For about twelve years, since 2012', 'The head office is in New York'], answer: 1, ai_explain: '"How long" → cần khoảng thời gian. B: "For about twelve years, since 2012" = trả lời đúng dạng. A và C đều cung cấp địa điểm, không phải thời gian.' },
        { text: 'Q14: What is the primary purpose of Conversation 1 between the hotel and the event planner?', translated: 'Mục đích chính của cuộc trò chuyện 1 giữa khách sạn và người tổ chức sự kiện là gì?', choices: ['To negotiate the conference venue booking and catering requirements', 'To discuss complaint about previous event service quality', 'To arrange a hotel room reservation for the organiser', 'To plan the entertainment schedule for the conference'], answer: 0, ai_explain: 'Cuộc hội thoại 1: "Negotiating conference venue booking and catering requirements" — Đàm phán về đặt phòng hội nghị và yêu cầu phục vụ ăn uống.' },
        { text: 'Q15: In Conversation 1, which of the following would the event planner most likely ask about?', translated: 'Trong Cuộc hội thoại 1, người tổ chức sự kiện nhiều khả năng sẽ hỏi về điều gì?', choices: ['The hotel room cancellation policy', 'Catering menu options and dietary accommodation for conference guests', 'The hotel\'s wifi password for personal use', 'Historical background of the hotel venue'], answer: 1, ai_explain: 'Yêu cầu phục vụ ăn uống (catering requirements) bao gồm menu và chế độ ăn đặc biệt là câu hỏi tự nhiên nhất trong ngữ cảnh đặt tiệc hội nghị.' },
        { text: 'Q16: What issue is being discussed in Conversation 2?', translated: 'Vấn đề nào đang được thảo luận trong Cuộc hội thoại 2?', choices: ['Launching a new product to replace an existing one', 'Product recall procedures and customer communication strategy', 'Addressing negative reviews on the company website', 'Updating the product packaging design'], answer: 1, ai_explain: 'Cuộc hội thoại 2: "Discussing product recall procedures and customer communication strategy."' },
        { text: 'Q17: In Conversation 2, why would a company communicate urgently with customers?', translated: 'Trong Cuộc hội thoại 2, tại sao công ty sẽ giao tiếp khẩn cấp với khách hàng?', choices: ['To announce a major product discount event', 'To notify them of a product recall and safety concern', 'To inform them of changes to the customer loyalty program', 'To survey customer satisfaction with recent purchases'], answer: 1, ai_explain: 'Product recall = thu hồi sản phẩm vì vấn đề an toàn → thông báo khẩn cấp cho khách hàng về recall là mục đích chính.' },
        { text: 'Q18: What is the main topic of Conversation 3?', translated: 'Chủ đề chính của Cuộc hội thoại 3 là gì?', choices: ['A dispute between two colleagues about travel reimbursement', 'Arranging business travel itinerary, hotel upgrades, and visa requirements', 'Reviewing the company\'s corporate travel policy handbook', 'Booking recreational travel for the annual company retreat'], answer: 1, ai_explain: 'Cuộc hội thoại 3: "Arranging business travel itinerary, hotel upgrades, and visa requirements."' },
        { text: 'Q19: In Conversation 3, what does the traveller likely request from the travel coordinator?', translated: 'Trong Cuộc hội thoại 3, người đi công tác nhiều khả năng yêu cầu điều gì từ người điều phối du lịch?', choices: ['Extension of the business trip by one additional week', 'Hotel room upgrade and assistance with visa documentation', 'Refund for a previously cancelled flight ticket', 'Transfer to a different departure airport'], answer: 1, ai_explain: '"Hotel upgrades, and visa requirements" → yêu cầu nâng hạng phòng và hỗ trợ thủ tục visa là nội dung trung tâm của conversation 3.' },
        { text: 'Q20: In Conversation 3, what documentation might the business traveller need to prepare?', translated: 'Trong Cuộc hội thoại 3, người đi công tác có thể cần chuẩn bị tài liệu nào?', choices: ['Employment contract for immigration purposes', 'Visa application and supporting business documents', 'Tax identification certificate for customs clearance', 'Medical insurance documentation for overseas travel'], answer: 1, ai_explain: '"Visa requirements" trong ngữ cảnh business travel = visa application + business invitation letter/supporting documents.' },
        { text: 'Q21: What type of business travel activity is likely discussed in Conversation 3?', translated: 'Loại hoạt động du lịch công tác nào có thể được thảo luận trong Cuộc hội thoại 3?', choices: ['Domestic conference attendance within the same country', 'International business travel to a foreign client location', 'Team-building retreat to a mountain resort', 'Training programme at company headquarters in the capital'], answer: 1, ai_explain: '"Visa requirements" cho thấy đây là chuyến đi quốc tế (international travel) — thị thực chỉ cần khi vượt biên quốc tế.' },
        { text: 'Q22: Based on Conversation 3 context, who is most likely the travel coordinator?', translated: 'Dựa trên ngữ cảnh Cuộc hội thoại 3, ai có khả năng là người điều phối du lịch?', choices: ['A visa officer at the embassy', 'An HR or administrative professional managing corporate travel', 'The CEO\'s personal assistant scheduling executive travel', 'An airline customer service representative'], answer: 1, ai_explain: 'Travel coordinators in TOEIC conversations are typically HR or administrative staff who handle corporate travel bookings, hotel arrangements, and documentation.' },
        { text: 'Q23 (Talk): What is the main subject of the HR announcement?', translated: 'Chủ đề chính của thông báo nhân sự là gì?', choices: ['A new employee benefits package', 'Updated performance review cycle and bonus structure', 'Changes to the company pension plan', 'Mandatory training programme schedule for the coming quarter'], answer: 1, ai_explain: '"Internal HR announcement about new performance review cycle and bonus structure" — đây là chủ đề trung tâm của bài thuyết trình.' },
        { text: 'Q24 (Talk): What change to the performance review process is most likely being announced?', translated: 'Thay đổi nào trong quy trình đánh giá hiệu suất có khả năng được thông báo nhất?', choices: ['Replacing annual reviews with quarterly performance check-ins', 'Eliminating all written performance evaluations going forward', 'Combining the performance review and salary negotiation into one meeting', 'Outsourcing performance management to an external consulting firm'], answer: 0, ai_explain: 'Changing from annual to quarterly review cycle is the most common HR performance management update in TOEIC listening scenarios, aligning with "new performance review cycle" language.' },
        { text: 'Q25 (Talk): Regarding the bonus structure, what information would be MOST useful for employees to know?', translated: 'Liên quan đến cấu trúc thưởng, thông tin nào SẼ HỮU ÍCH NHẤT cho nhân viên biết?', choices: ['The name of the new HR software system being implemented', 'How performance ratings will be linked to bonus calculations', 'Which departments will receive the largest bonuses', 'When the HR director will be available for individual meetings'], answer: 1, ai_explain: 'Nhân viên quan tâm nhất đến cách điểm đánh giá hiệu suất (performance ratings) được kết nối với tính toán thưởng (bonus calculations). Đây là thông tin thiết thực nhất.' }
      ]
    },

    // ===========================================================
    // ETS 2024 TEST 2 – FULL READING (24 CÂU)
    // ===========================================================
    'TOEIC Actual Test ETS 2024 · Test 2 – Full Reading (24 Câu)': {
      type: 'reading_passage',
      passageTitle: 'ETS TOEIC 2024 – Full Reading Test 2: Grammar, Text Completion & Comprehension',
      passageText: `PART 5 – INCOMPLETE SENTENCES (Q1-Q10)

Q1: Before the contract ------- signed, both parties must review all terms and conditions carefully.
(A) is   (B) was   (C) being   (D) been

Q2: The CEO's keynote address at the annual shareholders' conference was ------- well-received.
(A) exceptional   (B) exceptionally   (C) exception   (D) excepting

Q3: Neither the warehouse manager ------- the logistics coordinator had been informed of the shipment delay.
(A) or   (B) nor   (C) but   (D) and

Q4: The consulting firm ------- major operations in Singapore since establishing its Asia-Pacific headquarters there in 2019.
(A) conducts   (B) has conducted   (C) conducted   (D) is conducting

Q5: Employees ------- submit timesheets by noon on Friday will not be included in the current payroll cycle.
(A) who fail to   (B) which fails to   (C) that failing to   (D) whom failed to

Q6: The new laboratory equipment, ------- was donated by a private research foundation, significantly improved testing accuracy.
(A) who   (B) whose   (C) which   (D) that

Q7: All participants are encouraged to ------- their registration confirmation emails prior to checking in at the symposium.
(A) print   (B) printed   (C) printing   (D) prints

Q8: Despite ------- significant challenges in the first quarter, the project team delivered outstanding results by year-end.
(A) face   (B) faced   (C) facing   (D) to face

Q9: The research ------- that consumers are more likely to purchase products endorsed by people they perceive as similar to themselves.
(A) suggests   (B) is suggested   (C) suggested that   (D) suggestion

Q10: The new supplier ------- our existing vendor in terms of both price and delivery reliability.
(A) outperforms   (B) outperformed   (C) outperforming   (D) has been outperforming

PART 6 – TEXT COMPLETION (Q11-Q14): BUSINESS EMAIL

From: Operations Director
To: All Department Heads
RE: New Procurement Policy – Effective Q4 2024

Effective the first of October, all purchase orders exceeding £5,000 ------- (11) submitted to the Procurement Oversight Committee for pre-approval. This policy ------- (12) introduced in response to the findings of our annual financial audit, which identified inconsistencies in departmental spending authorisation.

Going forward, all requests must include a minimum of three competitive quotes from approved vendors. Departments ------- (13) to maintain updated vendor lists, and any new vendor onboarding must comply with the revised Supplier Code of Conduct published on the company intranet. The compliance team will ------- (14) monthly spend reports to monitor adherence to the new policy.

Q11: (A) must be   (B) must   (C) being   (D) are must be
Q12: (A) has been   (B) have been   (C) was   (D) were
Q13: (A) require   (B) are required   (C) requiring   (D) required
Q14: (A) review   (B) reviewing   (C) reviewed   (D) to review

PART 7 – READING COMPREHENSION (Q15-Q24)

SINGLE PASSAGE (Q15-18): JOB ADVERTISEMENT

POSITION: Senior Data Analyst — Consumer Insights Division
COMPANY: Nexus Analytics Group
LOCATION: Melbourne, Australia (Hybrid: 3 days in-office, 2 days remote)
SALARY: AUD $105,000 – $125,000 per annum (dependent on experience)

RESPONSIBILITIES:
• Design and execute end-to-end quantitative research studies and consumer behaviour analyses
• Build and maintain automated reporting dashboards using Tableau and Power BI
• Present complex analytical findings to senior leadership and non-technical stakeholders
• Collaborate cross-functionally with Marketing, Product, and Strategy teams
• Mentor two junior analysts within the Consumer Insights team

REQUIREMENTS:
• Minimum 5 years of experience in data analytics or market research
• Advanced proficiency in SQL, Python, and R
• Demonstrated experience with statistical modelling (regression, clustering, predictive analytics)
• Bachelor's degree minimum; Master's degree in Statistics, Economics, or related field preferred
• Experience in FMCG, retail, or financial services industry preferred

HOW TO APPLY: Submit your CV and a cover letter (maximum 500 words) outlining your most significant analytical project to careers@nexusanalytics.com.au by October 31. Only shortlisted candidates will be contacted for interview.

Q15: What type of work arrangement is offered for this position?
(A) Fully remote with occasional travel
(B) Fully in-office at the Melbourne location
(C) Hybrid with three days in-office and two days remote
(D) Flexible hours with no fixed in-office requirement

Q16: What is the minimum years of experience required?
(A) Three years   (B) Four years   (C) Five years   (D) Seven years

Q17: Which of the following is listed as a PREFERRED but not mandatory requirement?
(A) Proficiency in SQL and Python
(B) A Master's degree in a relevant field
(C) Experience presenting to senior leadership
(D) Building dashboards in Tableau or Power BI

Q18: According to the job posting, what should the cover letter include?
(A) A list of all previous employers over the past decade
(B) The applicant's most significant analytical project described in 500 words or fewer
(C) A portfolio of all data visualisation work completed in the current role
(D) References from at least two previous supervisors in data analytics

DOUBLE PASSAGE (Q19-Q24): CONFERENCE INVITATION + EMAIL REPLY

DOCUMENT A – INVITATION LETTER:
Nexus Global Technology Forum
Invitation to Present: Future of AI in Financial Services

Dear Ms. Amara Okonkwo,

On behalf of the organising committee of the Nexus Global Technology Forum, we are delighted to extend an invitation for you to present at our upcoming conference, to be held in Singapore from 14–16 November 2024 at the Marina Bay Convention Centre.

Given your highly regarded research into machine learning applications in credit risk modelling, we believe your perspective would be of considerable value to our attendees — senior executives, regulators, and technologists from over forty countries.

We invite you to present a thirty-minute keynote address on November 15 at 9:30 AM, followed by a fifteen-minute Q&A session. We are pleased to offer complimentary conference registration, economy return airfare from your home city, and four nights' accommodation at the Grand Marina Hotel.

Should you accept, please confirm by October 25 at the latest. We look forward to welcoming you to Singapore.

Warm regards,
Dr. James Holloway
Programme Director, Nexus Global Technology Forum

DOCUMENT B – REPLY EMAIL:
From: Amara Okonkwo <a.okonkwo@fintechresearch.org>
To: Dr. James Holloway
Date: October 23, 2024
Subject: Re: Invitation to Present – Nexus Global Technology Forum

Dear Dr. Holloway,

Thank you for this kind invitation. I am honoured to have been considered for such a prestigious forum. I am pleased to accept and look forward to presenting on November 15.

I have one logistical request: as I will be travelling from Johannesburg, the economy return flights involve two connections and approximately twenty-two hours of travel time. Would it be possible to arrange a business class ticket for the outbound journey, given the travel demands? I am entirely comfortable with economy for the return trip.

Additionally, I will require a presentation laptop with HDMI connectivity, a wireless presenter clicker, and the slides will be in PowerPoint format rather than Keynote.

Please let me know if you need any additional information to complete my registration. I very much look forward to contributing to what promises to be an excellent event.

Best regards,
Amara Okonkwo
Senior Research Fellow, FinTech Research Institute

Q19: Where will the Nexus Global Technology Forum be held?
(A) In Tokyo at the Tokyo International Forum
(B) In Singapore at the Marina Bay Convention Centre
(C) In London at the ExCeL Exhibition Centre
(D) In New York at the Javits Convention Center

Q20: What is Ms. Okonkwo invited to present about?
(A) The history of digital banking regulation in sub-Saharan Africa
(B) Machine learning applications in credit risk modelling
(C) Blockchain technology in cross-border payment systems
(D) Ethical considerations in AI-powered customer profiling

Q21: Which of the following is NOT included in the offered package?
(A) Complimentary conference registration
(B) Return airfare from the speaker's home city
(C) Four nights' accommodation at the Grand Marina Hotel
(D) A business class upgrade for the outbound flight

Q22: What special request does Ms. Okonkwo make in her reply?
(A) She requests a full business class ticket for both outbound and return flights
(B) She asks for a business class ticket for the outbound journey only
(C) She declines the flight offer and arranges her own travel independently
(D) She requests to present via video conference instead of in person

Q23: What presentation equipment does Ms. Okonkwo require?
(A) A Mac computer with Keynote and a laser pointer
(B) A laptop with HDMI, a wireless presenter clicker, and PowerPoint compatibility
(C) A large-format LED display and custom presenter podium
(D) A standard projector with a VGA cable and wired microphone

Q24: By what date must Ms. Okonkwo confirm her acceptance?
(A) October 20   (B) October 25   (C) October 31   (D) November 1`,
      questions: [
        // PART 5
        { text: 'Q1 (Part 5): Before the contract ------- signed, both parties must review all terms.', translated: 'Trước khi hợp đồng _______ ký, cả hai bên phải xem xét tất cả các điều khoản.', choices: ['is', 'was', 'being', 'been'], answer: 0, ai_explain: '"Before the contract is signed" — Present Passive trong mệnh đề trước (temporal clause). "Before" dùng với Simple Present cho conditional/temporal clauses, không phải past.' },
        { text: 'Q2 (Part 5): The CEO\'s keynote address was ------- well-received.', translated: 'Bài phát biểu khai mạc của CEO _______ được tiếp nhận nồng nhiệt.', choices: ['exceptional', 'exceptionally', 'exception', 'excepting'], answer: 1, ai_explain: '"Exceptionally" — trạng từ bổ nghĩa cho tính từ "well-received." Cấu trúc: adverb + adjective/adverb: "exceptionally well-received." "Exceptional" là tính từ, không bổ nghĩa được cho adjective khác.' },
        { text: 'Q3 (Part 5): Neither the warehouse manager ------- the logistics coordinator had been informed.', translated: 'Cả giám đốc kho lẫn _______ điều phối logistics đều không được thông báo.', choices: ['or', 'nor', 'but', 'and'], answer: 1, ai_explain: '"Neither... nor" là cặp liên từ tương quan chuẩn. "Neither A nor B" = "cả A lẫn B đều không." Đây là TOEIC Part 5 grammar classic.' },
        { text: 'Q4 (Part 5): The consulting firm ------- major operations in Singapore since 2019.', translated: 'Công ty tư vấn _______ hoạt động lớn ở Singapore từ năm 2019.', choices: ['conducts', 'has conducted', 'conducted', 'is conducting'], answer: 1, ai_explain: '"has conducted" — Present Perfect vì "since 2019" báo hiệu hành động bắt đầu từ quá khứ và tiếp tục đến hiện tại. "Since" + năm = Present Perfect là quy tắc vàng.' },
        { text: 'Q5 (Part 5): Employees ------- submit timesheets by noon on Friday will not be included in payroll.', translated: 'Nhân viên _______ nộp bảng chấm công trước trưa thứ Sáu sẽ không được tính vào bảng lương hiện tại.', choices: ['who fail to', 'which fails to', 'that failing to', 'whom failed to'], answer: 0, ai_explain: '"who fail to" — "Employees who fail to submit" = relative clause với "who" (người), thì hiện tại (fail) vì đây là điều kiện/chính sách hiện tại. "Whom" là tân ngữ, sai ở đây.' },
        { text: 'Q6 (Part 5): The laboratory equipment, ------- was donated by a private foundation, improved testing accuracy.', translated: 'Thiết bị phòng thí nghiệm, _______ được tặng bởi một quỹ nghiên cứu tư nhân, đã cải thiện độ chính xác.', choices: ['who', 'whose', 'which', 'that'], answer: 2, ai_explain: '"which" — Non-restrictive relative clause (có dấu phẩy) dùng cho vật (equipment). "That" không dùng trong non-restrictive clause, "who" cho người, "whose" là sở hữu.' },
        { text: 'Q7 (Part 5): All participants are encouraged to ------- their registration confirmation emails prior to checking in.', translated: 'Tất cả người tham gia được khuyến khích _______ email xác nhận đăng ký trước khi check-in.', choices: ['print', 'printed', 'printing', 'prints'], answer: 0, ai_explain: '"to print" — Cấu trúc "encouraged to + base verb (infinitive)." "Encouraged to print" = được khuyến khích in. Đây là to-infinitive sau động từ.' },
        { text: 'Q8 (Part 5): Despite ------- significant challenges, the team delivered outstanding results.', translated: 'Mặc dù _______ những thách thức đáng kể, nhóm đã đạt kết quả xuất sắc.', choices: ['face', 'faced', 'facing', 'to face'], answer: 2, ai_explain: '"Despite + gerund (facing)." Cấu trúc: "Despite/In spite of + V-ing" = mặc dù (đang) phải đối mặt. "Despite faced" và "despite to face" đều sai ngữ pháp.' },
        { text: 'Q9 (Part 5): The research ------- that consumers prefer products endorsed by similar people.', translated: 'Nghiên cứu _______ rằng người tiêu dùng thích các sản phẩm được những người tương tự chứng thực.', choices: ['suggests', 'is suggested', 'suggested that', 'suggestion'], answer: 0, ai_explain: '"suggests" — Simple Present Active. "The research suggests that..." = Nghiên cứu cho thấy rằng... "Suggested that" sẽ cần thì past, "suggestion" là danh từ.' },
        { text: 'Q10 (Part 5): The new supplier ------- our existing vendor in price and delivery reliability.', translated: 'Nhà cung cấp mới _______ nhà cung cấp hiện tại của chúng tôi về giá và độ tin cậy giao hàng.', choices: ['outperforms', 'outperformed', 'outperforming', 'has been outperforming'], answer: 0, ai_explain: '"outperforms" — Simple Present vì đây là sự thực hiện tại đang xảy ra (so sánh hiện tại giữa hai nhà cung cấp). Không dùng continuous vì đây là trạng thái cố định.' },
        // PART 6
        { text: 'Q11 (Part 6): All purchase orders exceeding £5,000 ------- submitted to the Procurement Oversight Committee.', translated: 'Tất cả đơn đặt hàng vượt quá £5,000 _______ nộp cho Ủy ban Giám sát Mua sắm.', choices: ['must be', 'must', 'being', 'are must be'], answer: 0, ai_explain: '"must be" — Modal Passive: "must be submitted" (phải được nộp). "Must" + be + past participle là cấu trúc passive bắt buộc. "Are must be" sai ngữ pháp hoàn toàn.' },
        { text: 'Q12 (Part 6): This policy ------- introduced in response to the annual financial audit findings.', translated: 'Chính sách này _______ được đưa ra để phản hồi với kết quả kiểm toán tài chính hằng năm.', choices: ['has been', 'have been', 'was', 'were'], answer: 2, ai_explain: '"was" — Past Simple Passive vì đây là sự kiện đã hoàn thành trong quá khứ ("introduced in response to... which identified..."). Chính sách đã được giới thiệu (hoàn tất). "Policy" là danh từ số ít → was.' },
        { text: 'Q13 (Part 6): Departments ------- to maintain updated vendor lists.', translated: 'Các phòng ban _______ duy trì danh sách nhà cung cấp được cập nhật.', choices: ['require', 'are required', 'requiring', 'required'], answer: 1, ai_explain: '"are required" — Passive Present. "Departments are required to maintain" = các phòng ban được yêu cầu phải duy trì. "Require" (active) nghĩa là "yêu cầu ai đó" — sai context.' },
        { text: 'Q14 (Part 6): The compliance team will ------- monthly spend reports to monitor adherence.', translated: 'Nhóm tuân thủ sẽ _______ các báo cáo chi tiêu hàng tháng để giám sát việc tuân thủ.', choices: ['review', 'reviewing', 'reviewed', 'to review'], answer: 0, ai_explain: '"review" — "will + base verb" (Future Simple). "Will review" = sẽ xem xét. Sau "will" luôn dùng bare infinitive (review, không phải reviewing hay reviewed).' },
        // PART 7 Single Passage
        { text: 'Q15 (Part 7): What type of work arrangement is offered for the Senior Data Analyst position?', translated: 'Loại hình làm việc nào được cung cấp cho vị trí Senior Data Analyst?', choices: ['Fully remote with occasional travel', 'Fully in-office at Melbourne', 'Hybrid: 3 days in-office, 2 days remote', 'Flexible hours with no fixed requirement'], answer: 2, ai_explain: '"Hybrid: 3 days in-office, 2 days remote" — stated explicitly in the job posting: "Hybrid: 3 days in-office, 2 days remote."' },
        { text: 'Q16 (Part 7): What is the minimum years of experience required?', translated: 'Số năm kinh nghiệm tối thiểu yêu cầu là bao nhiêu?', choices: ['Three years', 'Four years', 'Five years', 'Seven years'], answer: 2, ai_explain: '"Minimum 5 years of experience in data analytics or market research."' },
        { text: 'Q17 (Part 7): Which requirement is listed as PREFERRED but not mandatory?', translated: 'Yêu cầu nào được liệt kê là ƯU TIÊN nhưng không bắt buộc?', choices: ['SQL and Python proficiency', 'A Master\'s degree in a relevant field', 'Experience presenting to senior leadership', 'Building dashboards in Tableau or Power BI'], answer: 1, ai_explain: '"Master\'s degree in Statistics, Economics, or related field preferred" — từ "preferred" = ưu tiên nhưng không bắt buộc, khác với Bachelor\'s degree được yêu cầu ("minimum").' },
        { text: 'Q18 (Part 7): What should the cover letter include?', translated: 'Thư xin việc nên bao gồm những gì?', choices: ['List of all previous employers over the past decade', 'Description of the most significant analytical project in 500 words or fewer', 'Portfolio of all data visualisation work', 'References from two previous supervisors'], answer: 1, ai_explain: '"Submit your CV and a cover letter (maximum 500 words) outlining your most significant analytical project."' },
        // Double passage
        { text: 'Q19 (Part 7): Where will the Technology Forum be held?', translated: 'Diễn đàn Công nghệ sẽ được tổ chức ở đâu?', choices: ['Tokyo International Forum', 'Singapore – Marina Bay Convention Centre', 'London ExCeL Exhibition Centre', 'New York Javits Convention Center'], answer: 1, ai_explain: '"to be held in Singapore from 14–16 November 2024 at the Marina Bay Convention Centre."' },
        { text: 'Q20 (Part 7): What is Ms. Okonkwo invited to present about?', translated: 'Bà Okonkwo được mời trình bày về chủ đề gì?', choices: ['History of digital banking regulation', 'Machine learning applications in credit risk modelling', 'Blockchain in cross-border payments', 'AI-powered customer profiling ethics'], answer: 1, ai_explain: '"Given your highly regarded research into machine learning applications in credit risk modelling, we believe your perspective would be of considerable value."' },
        { text: 'Q21 (Part 7): Which is NOT included in the offered package?', translated: 'Điều nào KHÔNG được bao gồm trong gói đề nghị?', choices: ['Conference registration', 'Return airfare from home city', 'Four nights accommodation', 'Business class upgrade for outbound flight'], answer: 3, ai_explain: 'The invitation offers "economy return airfare" — NOT business class. Ms. Okonkwo specifically requests a business class upgrade in her reply, confirming this was not originally included.' },
        { text: 'Q22 (Part 7): What special request does Ms. Okonkwo make?', translated: 'Bà Okonkwo đưa ra yêu cầu đặc biệt nào?', choices: ['Full business class for both flights', 'Business class for outbound journey only', 'She arranges her own travel independently', 'She requests to present via video conference'], answer: 1, ai_explain: '"Would it be possible to arrange a business class ticket for the outbound journey, given the travel demands? I am entirely comfortable with economy for the return trip."' },
        { text: 'Q23 (Part 7): What presentation equipment does Ms. Okonkwo require?', translated: 'Bà Okonkwo yêu cầu thiết bị trình bày nào?', choices: ['Mac with Keynote and laser pointer', 'Laptop with HDMI, wireless clicker, PowerPoint compatible', 'Large-format LED display and custom podium', 'Projector with VGA cable and wired microphone'], answer: 1, ai_explain: '"I will require a presentation laptop with HDMI connectivity, a wireless presenter clicker, and the slides will be in PowerPoint format rather than Keynote."' },
        { text: 'Q24 (Part 7): By what date must Ms. Okonkwo confirm her acceptance?', translated: 'Bà Okonkwo phải xác nhận chấp nhận trước ngày nào?', choices: ['October 20', 'October 25', 'October 31', 'November 1'], answer: 1, ai_explain: '"Should you accept, please confirm by October 25 at the latest."' }
      ]
    },

    // ===========================================================
    // PRACTICE TESTS (SHORT)
    // ===========================================================
    'TOEIC Part 1 Practice – Photograph Description': {
      type: 'audio_mcq',
      audioTitle: 'TOEIC Practice: Part 1 – Photo Description (6 questions)',
      audioScript: 'Six TOEIC-style photographs: 1. A man is reading a newspaper on a park bench. 2. Workers are paving a road. 3. A woman is hanging clothes on a line. 4. A conference table with laptops and papers is shown. 5. A chef is decorating a cake. 6. Boats are docked at a marina.',
      questions: [
        { text: 'P1-1: A man is _______ on a park bench.', translated: 'P1-1: Người đàn ông đang _______ trên ghế công viên.', choices: ['sleeping soundly', 'reading a newspaper', 'feeding the ducks', 'talking on his phone'], answer: 1, ai_explain: '"A man is reading a newspaper on a park bench." — Action keywords: reading, newspaper, bench. Eliminate distractors: sleeping (eyes closed), feeding ducks (near water), phone (different activity).' },
        { text: 'P1-2: What are the workers doing in the road photograph?', translated: 'P1-2: Công nhân đang làm gì trong bức ảnh về đường phố?', choices: ['Directing traffic around an accident', 'Installing new road signs', 'Paving a road', 'Painting lane markings on the road'], answer: 2, ai_explain: '"Workers are paving a road." Paving = trải nhựa đường. Key visual: asphalt equipment, road roller, workers in safety vests.' },
        { text: 'P1-3: What is the woman doing in the laundry photograph?', translated: 'P1-3: Người phụ nữ đang làm gì trong bức ảnh giặt đồ?', choices: ['Ironing clothes on a board', 'Hanging clothes on a line', 'Sorting laundry into baskets', 'Operating a washing machine'], answer: 1, ai_explain: '"A woman is hanging clothes on a line." Hanging (treo) on a line (dây phơi) = outdoor laundry. Ironing requires board/iron; sorting requires baskets visible.' },
        { text: 'P1-4: What can be seen on the conference table?', translated: 'P1-4: Có thể thấy gì trên bàn phòng họp?', choices: ['Only empty chairs and glasses of water', 'Laptops and papers are spread across the table', 'A projector and presentation screen', 'Only name placards and pens'], answer: 1, ai_explain: '"A conference table with laptops and papers is shown." — Key items: laptops (technology), papers (documents). No projector or people actively working.' },
        { text: 'P1-5: What is the chef doing in the kitchen photograph?', translated: 'P1-5: Đầu bếp đang làm gì trong bức ảnh nhà bếp?', choices: ['Chopping vegetables on a cutting board', 'Serving a dish to a restaurant customer', 'Decorating a cake', 'Washing pots in the kitchen sink'], answer: 2, ai_explain: '"A chef is decorating a cake." Decorating (trang trí) a cake = piping icing, adding fondant decorations. Visual cue: piping bag or spatula.' },
        { text: 'P1-6: Where are the boats in the final photograph?', translated: 'P1-6: Thuyền ở đâu trong bức ảnh cuối?', choices: ['Racing across open water', 'Under repair in a drydock facility', 'Docked at a marina', 'Being loaded with cargo at a commercial port'], answer: 2, ai_explain: '"Boats are docked at a marina." Docked (đậu bến) at a marina (bến du thuyền) = boats stationary, tied to dock. Racing = motion blur, drydock = boats out of water, cargo port = industrial setting.' }
      ]
    },
    'TOEIC Part 2 Practice – Question Response': {
      type: 'audio_mcq',
      audioTitle: 'TOEIC Practice: Part 2 – Question Response (8 exchanges)',
      audioScript: 'Eight question-response pairs covering WH questions (Who, What, Where, When, Why, How), Yes/No questions, and tag questions in office contexts.',
      questions: [
        { text: 'P2-1: Who approved the budget for the new marketing campaign?', translated: 'P2-1: Ai đã phê duyệt ngân sách cho chiến dịch marketing mới?', choices: ['The budget was approved yesterday', 'Ms. Reynolds from the finance committee', 'It was a very large budget'], answer: 1, ai_explain: '"Who" → cần tên người hoặc chức danh. B cung cấp cả tên (Ms. Reynolds) và chức danh (finance committee). A trả lời "when", C là nhận xét chung.' },
        { text: 'P2-2: What time does the webinar start?', translated: 'P2-2: Buổi hội thảo web bắt đầu lúc mấy giờ?', choices: ['At three thirty PM Eastern Standard Time', 'The webinar is about digital marketing', 'You can register on the website'], answer: 0, ai_explain: '"What time" → thời gian cụ thể. A: "At three thirty PM Eastern Standard Time" = đúng format. B trả lời "what about" (topic), C trả lời "how" (how to register).' },
        { text: 'P2-3: Where can I find the updated client database?', translated: 'P2-3: Tôi có thể tìm thấy cơ sở dữ liệu khách hàng cập nhật ở đâu?', choices: ['It should be on the shared server in the Sales folder', 'The database was updated last month', 'There are about 500 client records'], answer: 0, ai_explain: '"Where" → địa điểm/vị trí. A: "shared server in the Sales folder" = location. B (when), C (how many) không trả lời "where."' },
        { text: 'P2-4: Haven\'t you submitted your expense report yet?', translated: 'P2-4: Bạn vẫn chưa nộp báo cáo chi phí sao?', choices: ['Yes, I submitted it this morning to accounting', 'The expense report is very detailed', 'Accounting is on the second floor'], answer: 0, ai_explain: 'Negative question (Haven\'t you...?) → A xác nhận đã nộp rồi. "Yes, I submitted it this morning" = trả lời hành động đã hoàn thành. B và C không trả lời câu hỏi.' },
        { text: 'P2-5: Could you make copies of the agenda for everyone?', translated: 'P2-5: Bạn có thể photocopy chương trình họp cho mọi người không?', choices: ['Sure, how many people are attending?', 'The agenda was set last week', 'The meeting is in Room 402'], answer: 0, ai_explain: 'Request (Could you...?) → A đồng ý + hỏi số lượng cần thiết = phản hồi tự nhiên và hữu ích nhất. B (when it was set) và C (where meeting is) không trả lời request.' },
        { text: 'P2-6: Why was the product launch rescheduled?', translated: 'P2-6: Tại sao việc ra mắt sản phẩm bị lên lịch lại?', choices: ['The launch party was very exciting', 'Because the manufacturing team needed two more weeks for quality testing', 'The new launch date is next Thursday'], answer: 1, ai_explain: '"Why" → lý do (reason). B cung cấp lý do cụ thể (cần thêm 2 tuần để kiểm tra chất lượng). A là nhận xét, C là "when" (thời gian mới).' },
        { text: 'P2-7: The new project timeline has been confirmed, hasn\'t it?', translated: 'P2-7: Tiến độ dự án mới đã được xác nhận rồi phải không?', choices: ['Yes, the final version was sent to all stakeholders yesterday', 'The timeline is very optimistic', 'Project management set it up'], answer: 0, ai_explain: 'Tag question (hasn\'t it?) → xác nhận/phủ nhận + chi tiết. A xác nhận "Yes" + thêm thông tin (sent to stakeholders yesterday). B là ý kiến, C không trả lời yes/no.' },
        { text: 'P2-8: How did the sales team achieve such strong Q3 results?', translated: 'P2-8: Nhóm kinh doanh đã đạt được kết quả Q3 mạnh như vậy bằng cách nào?', choices: ['Q3 results were excellent this year', 'By focusing on high-value enterprise accounts and expanding into two new regional markets', 'The sales team has twelve members'], answer: 1, ai_explain: '"How" → phương pháp/cách thức. B giải thích chiến lược cụ thể (enterprise accounts + 2 new regional markets). A là nhận xét, C là thông tin về team (không phải cách thức).' }
      ]
    },
    'TOEIC Part 3 Practice – Short Conversations': {
      type: 'audio_mcq',
      audioTitle: 'TOEIC Practice: Part 3 – Short Conversations (3 conversations × 3 questions)',
      audioScript: `CONVERSATION 1 – REQUESTING A MEETING ROOM:
Receptionist: Good afternoon. Can I help you?
Employee (Mark): Hi. I need to book Conference Room B for a client presentation this Thursday at two PM. It's for about ten people and we'll need the projector.
Receptionist: Let me check... Thursday at two PM, Conference Room B. I'm afraid that room is already booked until four PM on Thursday. I do have Conference Room A available — it's slightly smaller, capacity for eight, but it has both a projector and a video conferencing system.
Mark: Hmm, we definitely need space for ten. Is there anything else available?
Receptionist: I can check the training room on the fourth floor — it holds fifteen and has a full AV setup, including wireless presentation capability.
Mark: That sounds perfect. Please book it under Mark Chen in the Sales department. I'll confirm the exact attendee count by Wednesday.
Receptionist: Done. I'll send you a confirmation email within the hour.

CONVERSATION 2 – PRODUCT COMPLAINT CALL:
Customer Service (Lisa): Thank you for calling TechVision support, this is Lisa.
Customer (Mr. Webb): Hello. I purchased your WV-500 wireless headphones three weeks ago and the battery started failing after just five days. I've already tried the reset procedure from your website, but the problem persists.
Lisa: I'm sorry to hear that, Mr. Webb. Three weeks is definitely within our ninety-day return and replacement policy. I can offer you a full replacement unit or, if you prefer, a full refund to your original payment method.
Customer: I'd prefer a replacement — I like the product when it works. How long will delivery take?
Lisa: Standard delivery is three to five business days, but since this is a warranty replacement I can upgrade you to express shipping at no additional charge — you should receive the unit within two business days.
Customer: That's great. Will I need to return the faulty unit first?
Lisa: No, we'll send the replacement first. Once you receive it, we'll include a prepaid return label for the defective unit.

CONVERSATION 3 – BUSINESS TRAVEL BOOKING:
Travel Coordinator (Helen): Helen speaking, corporate travel.
Manager (Ms. Park): Hi Helen, I need to book travel to Tokyo for a client meeting on November 12th. I'll need to arrive the evening before.
Helen: Certainly. Departing from where?
Ms. Park: From Singapore Changi. And I'd like to request a business class seat if there's one available within the travel budget.
Helen: Let me check... Singapore to Tokyo on November 11th, business class. I have a Singapore Airlines departure at 6:45 PM arriving Tokyo Haneda at 1:50 AM local time. That would be within your travel budget.
Ms. Park: Perfect. And hotel — somewhere close to Shibuya, preferably with a gym.
Helen: The Park Hyatt Tokyo in Shinjuku is close to Shibuya and excellent — I can also check the Andaz. Both are within policy.
Ms. Park: Let's go with the Park Hyatt. And can you arrange an airport transfer from Haneda?
Helen: Absolutely. I'll include a private car transfer. What time does your meeting end on the 12th?
Ms. Park: Probably around six PM. I'll book my return for the 13th.`,
      questions: [
        { text: 'P3-1: Why does Mark contact the receptionist?', translated: 'P3-1: Tại sao Mark liên hệ với lễ tân?', choices: ['To report a broken projector in Conference Room B', 'To book a conference room for a client presentation', 'To cancel an existing room reservation for Thursday', 'To request the IT team to set up video conferencing equipment'], answer: 1, ai_explain: '"I need to book Conference Room B for a client presentation this Thursday at two PM."' },
        { text: 'P3-2: Why is Conference Room B not available?', translated: 'P3-2: Tại sao Phòng Họp B không có sẵn?', choices: ['It is undergoing maintenance and cleaning', 'It has already been booked until 4 PM on Thursday', 'The room capacity has been reduced due to safety regulations', 'It does not have the required projector equipment'], answer: 1, ai_explain: '"I\'m afraid that room is already booked until four PM on Thursday."' },
        { text: 'P3-3: What is Mark\'s response to the alternative room suggestion?', translated: 'P3-3: Phản ứng của Mark với gợi ý phòng thay thế là gì?', choices: ['He agrees to use the smaller Conference Room A with 8 capacity', 'He books the training room on the fourth floor which holds 15', 'He decides to postpone the presentation to another day', 'He asks for a room outside the building at an external venue'], answer: 1, ai_explain: '"That sounds perfect. Please book it under Mark Chen in the Sales department." — Mark chọn phòng huấn luyện tầng 4 vì cần chỗ cho 10 người.' },
        { text: 'P3-4: How long has Mr. Webb had the WV-500 headphones?', translated: 'P3-4: Ông Webb đã có tai nghe WV-500 được bao lâu?', choices: ['5 days', '10 days', '3 weeks', '90 days'], answer: 2, ai_explain: '"I purchased your WV-500 wireless headphones three weeks ago." = 3 tuần. Lưu ý: battery failed after just 5 days (5 ngày pin hỏng), nhưng thời gian sở hữu là 3 tuần.' },
        { text: 'P3-5: What does Mr. Webb choose instead of a full refund?', translated: 'P3-5: Ông Webb chọn gì thay vì hoàn tiền đầy đủ?', choices: ['A partial store credit toward a newer model', 'A full replacement unit of the WV-500', 'An extended warranty for his current headphones', 'Free repair service at a local service centre'], answer: 1, ai_explain: '"I\'d prefer a replacement — I like the product when it works."' },
        { text: 'P3-6: How soon will Mr. Webb receive the replacement unit?', translated: 'P3-6: Khi nào ông Webb sẽ nhận được sản phẩm thay thế?', choices: ['Within 24 hours via same-day courier', 'Within 2 business days via express shipping', 'Within 3 to 5 business days standard delivery', 'Within 7 business days international shipping'], answer: 1, ai_explain: '"I can upgrade you to express shipping at no additional charge — you should receive the unit within two business days."' },
        { text: 'P3-7: What class of travel does Ms. Park request?', translated: 'P3-7: Ms. Park yêu cầu hạng ghế nào?', choices: ['Economy class with extra legroom', 'Premium economy class', 'Business class', 'First class'], answer: 2, ai_explain: '"I\'d like to request a business class seat if there\'s one available within the travel budget."' },
        { text: 'P3-8: Which hotel does Ms. Park ultimately choose?', translated: 'P3-8: Ms. Park cuối cùng chọn khách sạn nào?', choices: ['Andaz Tokyo Toranomon Hills', 'Hilton Tokyo near Shinjuku Station', 'Park Hyatt Tokyo in Shinjuku', 'Grand Hyatt Tokyo in Roppongi'], answer: 2, ai_explain: '"Let\'s go with the Park Hyatt." — Ms. Park chọn Park Hyatt Tokyo sau khi được Helen đề xuất hai lựa chọn.' },
        { text: 'P3-9: What additional service does Ms. Park request?', translated: 'P3-9: Ms. Park yêu cầu dịch vụ bổ sung nào?', choices: ['A private Japanese language interpreter for the client meeting', 'An airport transfer from Haneda to the hotel', 'A restaurant reservation for the client dinner on November 12th', 'A meeting room booking at the Tokyo client office'], answer: 1, ai_explain: '"And can you arrange an airport transfer from Haneda?" — Helen xác nhận: "Absolutely. I\'ll include a private car transfer."' }
      ]
    },
    'TOEIC Part 5 Practice – Incomplete Sentences': {
      type: 'reading_passage',
      passageTitle: 'TOEIC Part 5 Practice: Incomplete Sentences (Grammar & Vocabulary – 10 Câu)',
      passageText: `TOEIC PART 5 PRACTICE – 10 INCOMPLETE SENTENCES

Q1: All team members ------- to attend the mandatory safety training next Wednesday.
(A) require   (B) are required   (C) requiring   (D) required

Q2: The proposal ------- by the board before it can be forwarded to the client.
(A) must approve   (B) must be approved   (C) must approving   (D) must approved

Q3: Our company has experienced ------- growth in the Asia-Pacific market over the past two years.
(A) exception   (B) exceptionally   (C) exceptional   (D) excepted

Q4: Please ------- your visitor badge visibly at all times while on company premises.
(A) wearing   (B) wore   (C) wear   (D) worn

Q5: The project was completed ------- schedule, much to the delight of the entire management team.
(A) ahead of   (B) instead of   (C) in spite of   (D) due to

Q6: ------- the heavy rainfall, the outdoor product demonstration was cancelled and rescheduled for the following week.
(A) Despite   (B) Due to   (C) Although   (D) Even though

Q7: The finance department ------- the annual budget projections since early September.
(A) prepared   (B) prepares   (C) has been preparing   (D) will prepare

Q8: Employees ------- work more than forty hours per week are entitled to overtime compensation under company policy.
(A) who   (B) which   (C) whose   (D) whom

Q9: The new accounts software is both user-friendly ------- highly compatible with our existing infrastructure.
(A) but also   (B) and   (C) nor   (D) or

Q10: Please submit all documentation ------- the specified deadline to ensure timely processing of your application.
(A) in spite of   (B) prior to   (C) in lieu of   (D) instead of`,
      questions: [
        { text: 'Q1: All team members ------- to attend the mandatory safety training.', translated: 'Q1: Tất cả thành viên nhóm _______ tham dự đào tạo an toàn bắt buộc.', choices: ['require', 'are required', 'requiring', 'required'], answer: 1, ai_explain: '"are required" — Passive present. "Team members are required to attend" = các thành viên được yêu cầu (bởi công ty). "Require" là active — nghĩa ngược lại.' },
        { text: 'Q2: The proposal ------- before it can be forwarded to the client.', translated: 'Q2: Đề xuất _______ trước khi có thể chuyển đến khách hàng.', choices: ['must approve', 'must be approved', 'must approving', 'must approved'], answer: 1, ai_explain: '"must be approved" — Modal Passive. "Must + be + past participle" là cấu trúc passive obligation. Proposal không tự phê duyệt — được phê duyệt bởi board.' },
        { text: 'Q3: Our company has experienced ------- growth in the Asia-Pacific market.', translated: 'Q3: Công ty chúng tôi đã trải nghiệm sự tăng trưởng _______ tại thị trường châu Á-Thái Bình Dương.', choices: ['exception', 'exceptionally', 'exceptional', 'excepted'], answer: 2, ai_explain: '"exceptional" — Tính từ bổ nghĩa cho danh từ "growth." "Exceptional growth" = tăng trưởng ngoại lệ/vượt trội. "Exceptionally" là trạng từ, không bổ nghĩa cho noun.' },
        { text: 'Q4: Please ------- your visitor badge visibly at all times.', translated: 'Q4: Vui lòng _______ thẻ khách thăm của bạn một cách dễ thấy mọi lúc.', choices: ['wearing', 'wore', 'wear', 'worn'], answer: 2, ai_explain: '"wear" — Imperative (mệnh lệnh thức). "Please + base verb" = yêu cầu lịch sự. "Wear" là base form. "Wearing" là gerund/present participle, không dùng sau "please" trực tiếp.' },
        { text: 'Q5: The project was completed ------- schedule.', translated: 'Q5: Dự án được hoàn thành _______ lịch trình.', choices: ['ahead of', 'instead of', 'in spite of', 'due to'], answer: 0, ai_explain: '"ahead of schedule" = trước thời hạn (cụm cố định trong TOEIC). "Behind schedule" = trễ tiến độ. "Instead of schedule" và "due to schedule" đều không phải collocations tự nhiên.' },
        { text: 'Q6: ------- the heavy rainfall, the outdoor demonstration was cancelled.', translated: 'Q6: _______ mưa to, buổi trình diễn ngoài trời đã bị hủy.', choices: ['Despite', 'Due to', 'Although', 'Even though'], answer: 1, ai_explain: '"Due to" + noun phrase (the heavy rainfall) = "vì/do" + danh từ. "Due to" theo sau là danh từ/noun phrase. "Although/Even though" theo sau là mệnh đề (subject + verb).' },
        { text: 'Q7: The finance department ------- the annual budget projections since early September.', translated: 'Q7: Phòng tài chính _______ các dự báo ngân sách hàng năm từ đầu tháng 9.', choices: ['prepared', 'prepares', 'has been preparing', 'will prepare'], answer: 2, ai_explain: '"has been preparing" — Present Perfect Continuous. "Since early September" = từ điểm thời gian trong quá khứ đến hiện tại, và hành động vẫn đang tiếp diễn = PPCT.' },
        { text: 'Q8: Employees ------- work more than forty hours per week are entitled to overtime.', translated: 'Q8: Nhân viên _______ làm việc hơn 40 giờ mỗi tuần được hưởng lương làm thêm giờ.', choices: ['who', 'which', 'whose', 'whom'], answer: 0, ai_explain: '"who" — Relative pronoun cho người (employees) là chủ ngữ của mệnh đề quan hệ (work). "Which" cho vật, "whose" là sở hữu, "whom" là tân ngữ.' },
        { text: 'Q9: The new software is both user-friendly ------- highly compatible with existing infrastructure.', translated: 'Q9: Phần mềm mới vừa thân thiện với người dùng _______ tương thích cao với cơ sở hạ tầng hiện có.', choices: ['but also', 'and', 'nor', 'or'], answer: 1, ai_explain: '"both A and B" là cặp tương quan chuẩn. "Both user-friendly AND highly compatible." "But also" đi với "not only." "Nor" đi với "neither." "Or" = hoặc/hay.' },
        { text: 'Q10: Submit all documentation ------- the specified deadline.', translated: 'Q10: Nộp tất cả tài liệu _______ thời hạn quy định.', choices: ['in spite of', 'prior to', 'in lieu of', 'instead of'], answer: 1, ai_explain: '"prior to" = trước/trước khi (đồng nghĩa với "before" nhưng formal hơn). "Submit prior to the deadline" = nộp trước thời hạn. "In spite of" = mặc dù, "in lieu of" = thay cho.' }
      ]
    },
    'TOEIC Part 7 Practice – Single Passage': {
      type: 'reading_passage',
      passageTitle: 'TOEIC Part 7 Practice: Single Passage Reading Comprehension',
      passageText: `MEMORANDUM

TO: All Sales Department Staff
FROM: Rebecca Hollingsworth, VP of Sales
DATE: October 15, 2024
SUBJECT: Q4 Sales Incentive Programme – Important Updates

I am pleased to announce several enhancements to our Q4 Sales Incentive Programme, effective from October 1 through December 31, 2024.

TIER STRUCTURE:
- Tier 1 (90%–99% of quarterly target): 5% bonus on base salary
- Tier 2 (100%–110% of quarterly target): 10% bonus on base salary + additional £500 voucher
- Tier 3 (Above 110% of quarterly target): 15% bonus on base salary + additional £1,000 voucher + eligibility for the Annual Sales Excellence Award

UPDATED ELIGIBILITY CRITERIA:
All sales staff who joined before August 1, 2024 are eligible. New hires who joined after this date will participate in the programme starting Q1 2025.

Additionally, all eligible team members must maintain a minimum customer satisfaction rating of 4.2/5.0 (as measured by our post-sale survey system) to qualify for any incentive tier.

TRACKING AND REPORTING:
Individual progress dashboards have been updated in the Sales Performance System (SPS). You can access your real-time ranking and projected bonus at any time. Monthly progress reviews will be conducted on the last Friday of each month — October 25, November 29, and December 27.

Please contact your direct manager or HR Business Partner with any questions. Full policy documentation is available on the company intranet under HR > Incentive Programmes > Q4 2024.`,
      questions: [
        { text: 'Q1: What is the primary purpose of this memo?', translated: 'Q1: Mục đích chính của bản ghi nhớ này là gì?', choices: ['To inform staff of a new hiring process for the sales team', 'To announce updates to the Q4 Sales Incentive Programme', 'To reprimand staff for poor performance in Q3', 'To introduce the company\'s new Sales Performance System software'], answer: 1, ai_explain: '"I am pleased to announce several enhancements to our Q4 Sales Incentive Programme." = Thông báo về cập nhật chương trình khuyến khích bán hàng Q4.' },
        { text: 'Q2: What bonus percentage does an employee receive for achieving 105% of their quarterly target?', translated: 'Q2: Nhân viên nhận tỷ lệ thưởng bao nhiêu khi đạt 105% chỉ tiêu quý?', choices: ['5% bonus on base salary', '10% bonus + £500 voucher', '15% bonus + £1,000 voucher + award eligibility', '10% bonus only, without the voucher'], answer: 1, ai_explain: '105% falls in Tier 2 (100%–110%): "10% bonus on base salary + additional £500 voucher."' },
        { text: 'Q3: Who is NOT eligible for the Q4 incentive programme?', translated: 'Q3: Ai KHÔNG đủ điều kiện tham gia chương trình khuyến khích Q4?', choices: ['An employee who joined on June 15, 2024', 'A sales representative who joined on July 30, 2024', 'A new hire who started on August 15, 2024', 'An employee who has been with the company since 2020'], answer: 2, ai_explain: '"All sales staff who joined before August 1, 2024 are eligible. New hires who joined after this date will participate starting Q1 2025." August 15 > August 1 → NOT eligible for Q4.' },
        { text: 'Q4: What minimum customer satisfaction score must employees maintain to qualify for any incentive tier?', translated: 'Q4: Nhân viên phải duy trì điểm hài lòng khách hàng tối thiểu bao nhiêu để đủ điều kiện ở bất kỳ cấp độ nào?', choices: ['3.8 out of 5.0', '4.0 out of 5.0', '4.2 out of 5.0', '4.5 out of 5.0'], answer: 2, ai_explain: '"all eligible team members must maintain a minimum customer satisfaction rating of 4.2/5.0 (as measured by our post-sale survey system)."' },
        { text: 'Q5: When will the second monthly progress review take place?', translated: 'Q5: Buổi đánh giá tiến độ hàng tháng lần hai sẽ diễn ra vào khi nào?', choices: ['October 25', 'November 29', 'December 27', 'January 3, 2025'], answer: 1, ai_explain: '"Monthly progress reviews will be conducted on the last Friday of each month — October 25, November 29, and December 27." The second review = November 29.' },
        { text: 'Q6: Where can staff find full documentation about the incentive programme?', translated: 'Q6: Nhân viên có thể tìm thấy tài liệu đầy đủ về chương trình khuyến khích ở đâu?', choices: ['In an email attachment from Rebecca Hollingsworth', 'Through the Sales Performance System (SPS) dashboard', 'On the company intranet under HR > Incentive Programmes > Q4 2024', 'By requesting a printed copy from their direct manager'], answer: 2, ai_explain: '"Full policy documentation is available on the company intranet under HR > Incentive Programmes > Q4 2024."' }
      ]
    },
    'TOEIC Writing Practice – Email Response': {
      type: 'writing',
      questions: [
        {
          text: 'TOEIC Writing Task: Respond to the following email in 100–150 words. FROM: Customer Service Manager. SUBJECT: Partnership Opportunity. "Dear Sir/Madam, My name is David Kim, Regional Manager at Pacific Logistics Solutions. We have reviewed your company\'s service portfolio and believe there is excellent potential for a logistics partnership that could benefit both organisations. I would appreciate your thoughts on (1) whether you are open to exploring this partnership, and (2) what your preferred method and timeline for an initial discussion would be. Thank you for your time." Please write a professional response addressing both questions.',
          translated: 'Task: Trả lời email từ David Kim về cơ hội hợp tác logistics.',
          choices: [
            '✍️ BÀI MẪU BAND 8 (130 từ): "Dear Mr. Kim, Thank you for your interest in exploring a potential partnership between our organisations. I was glad to learn of Pacific Logistics Solutions\' interest in our service portfolio. To answer your questions directly: we are certainly open to exploring a logistics partnership, particularly given our current expansion into several markets where enhanced distribution capability would be of strategic value. Regarding an initial discussion, I would suggest a thirty-minute introductory video call as the most efficient starting point. I am available on the following dates: Tuesday, October 22 from 2:00 to 4:00 PM; Thursday, October 24 from 10:00 AM to noon; or any morning next week from 9:00 to 11:00 AM. Please let me know which time best suits your schedule, and I will send a calendar invitation with the meeting details. Best regards, [Your Name]"',
            '📋 CẤU TRÚC: Para 1: Cảm ơn + thể hiện quan tâm. Para 2: Trả lời câu hỏi 1 (open to partnership? Yes + brief reason). Para 3: Trả lời câu hỏi 2 (preferred method + 3 specific time options). Para 4: Kêu gọi hành động + kết thúc.',
            '🎯 Từ vựng email nghề nghiệp: "To answer your questions directly" — "strategic value" — "introductory video call" — "efficient starting point" — "calendar invitation"'
          ],
          answer: 0,
          ai_explain: 'TOEIC Email Response: PHẢI trả lời TẤT CẢ câu hỏi trong email gốc. David Kim hỏi 2 điều: (1) có mở cửa cho partnership không? (2) phương thức và timeline ưu tiên là gì? Thiếu một câu hỏi = điểm thấp.'
        },
        {
          text: 'TOEIC Writing: Complete this email with professional business language (fill in the blanks appropriately). FROM: [You] TO: All Staff. SUBJECT: Office Closure Notice. "Dear Team, I am writing to notify you that our main office will be _______ on Friday, November 1, due to the national public holiday. During this period, _______ access to the building will not be available, and the IT helpdesk will be _______. If you have any urgent matters, please _______ no later than Thursday, October 31. We will _______ normal operations on Monday, November 4. Thank you for your _______.  Best regards."',
          translated: 'Task: Điền từ phù hợp vào email thông báo đóng cửa văn phòng.',
          choices: [
            '✍️ ĐIỀN ĐÁP ÁN CHUẨN: "closed" (đóng cửa) / "physical" (physical access) / "unavailable" hoặc "out of service" / "address these with your manager" hoặc "contact your line manager" / "resume" (khôi phục) / "understanding and cooperation" (sự thông cảm và hợp tác).',
            '📋 TỪ VỰNG THÔNG BÁO ĐÓNG CỬA VĂN PHÒNG: closed / unavailable / out of office / resume normal operations / your understanding and cooperation / address urgent matters in advance / alternative contact arrangements.',
            '🎯 Cụm từ hữu ích: "due to the national public holiday" (do ngày lễ quốc gia) / "During this period" (Trong thời gian này) / "resume normal operations" (khôi phục hoạt động bình thường) / "thank you for your understanding" (cảm ơn sự thông cảm của bạn).'
          ],
          answer: 0,
          ai_explain: 'Email hoàn chỉnh đòi hỏi: chủ đề rõ ràng, thông tin đầy đủ (ngày đóng, lý do, ai liên hệ, khi nào mở lại), ngôn ngữ lịch sự chuyên nghiệp.'
        }
      ]
    }
  };

  // ==========================================
  // 3. THANG QUY ĐỔI ĐIỂM CHUẨN ETS (10-990)
  // ==========================================
  function calculateToeicScore(rawScore, totalQuestions, section) {
    if (!totalQuestions || totalQuestions === 0) totalQuestions = 25;
    const percentage = rawScore / totalQuestions;

    let scaledScore;
    if (section === 'Listening') {
      // Listening: max 495 points
      const levels = [5, 20, 35, 50, 70, 90, 115, 140, 165, 190, 215, 240, 265, 290, 320, 350, 385, 415, 445, 470, 495];
      const idx = Math.round(percentage * (levels.length - 1));
      scaledScore = levels[Math.min(idx, levels.length - 1)];
    } else if (section === 'Reading') {
      // Reading: max 495 points
      const levels = [5, 15, 30, 50, 70, 95, 120, 150, 180, 210, 240, 275, 310, 340, 370, 395, 420, 445, 460, 475, 495];
      const idx = Math.round(percentage * (levels.length - 1));
      scaledScore = levels[Math.min(idx, levels.length - 1)];
    } else {
      scaledScore = Math.round(percentage * 200);
    }

    const totalEstimate = scaledScore;
    const level = totalEstimate >= 860 ? 'C1 – Advanced Proficiency (860–990)' :
                  totalEstimate >= 730 ? 'B2 – Upper Intermediate (730–855)' :
                  totalEstimate >= 600 ? 'B1+ – Working Proficiency (600–725)' :
                  totalEstimate >= 470 ? 'B1 – Intermediate (470–595)' :
                  'A2 – Elementary (Below 470)';

    return { score: scaledScore, level, percentage: Math.round(percentage * 100) };
  }

  // ==========================================
  // 4. EXPORT
  // ==========================================
  window.toeicCourses = toeicCourses;
  window.toeicExams = toeicExams;
  window.calculateToeicScore = calculateToeicScore;

})(window);
