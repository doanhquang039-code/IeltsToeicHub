# -*- coding: utf-8 -*-
import sys
import re

html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# We will replace from "const courses = [" up to "updateScores();" before </script>
start_marker = "const courses = ["
end_marker = "renderCourses();\n    showWord(0);\n    updateScores();"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error: Markers not found! start_idx={start_idx}, end_idx={end_idx}")
    sys.exit(1)

new_js = '''// ==========================================
    // 1. NGÂN HÀNG ĐỀ THI 4 KỸ NĂNG: TOEIC & IELTS
    // ==========================================
    const courses = [
      // --- TOEIC ---
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 1: Photographs', 
        detail: 'Xem tranh công sở & chọn miêu tả chuẩn xác', 
        questions: 4, 
        time: '6 phút', 
        mark: 'L1',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 2: Question–Response', 
        detail: 'Nghe câu hỏi và chọn phản hồi giao tiếp thương mại', 
        questions: 5, 
        time: '8 phút', 
        mark: 'L2',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 3: Short Conversations', 
        detail: 'Hội thoại nơi làm việc & đàm phán hợp đồng', 
        questions: 3, 
        time: '6 phút', 
        mark: 'L3',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 5: Incomplete Sentences', 
        detail: 'Ngữ pháp, từ loại và liên từ trọng điểm', 
        questions: 5, 
        time: '6 phút', 
        mark: 'R5',
        type: 'mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 6: Text Completion', 
        detail: 'Điền từ và câu vào thư điện tử nội bộ', 
        questions: 4, 
        time: '7 phút', 
        mark: 'R6',
        type: 'reading_passage'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 7: Reading Comprehension', 
        detail: 'Đọc thông báo tuyển dụng và hóa đơn kinh doanh', 
        questions: 4, 
        time: '9 phút', 
        mark: 'R7',
        type: 'reading_passage'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Speaking', 
        title: 'TOEIC Speaking · Describe Picture & Opinion', 
        detail: 'Miêu tả hình ảnh và bày tỏ quan điểm văn phòng', 
        questions: 2, 
        time: '8 phút', 
        mark: 'SW',
        type: 'speaking'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Writing', 
        title: 'TOEIC Writing · Email Reply & Opinion Essay', 
        detail: 'Phản hồi thư khách hàng và viết đoạn văn nêu quan điểm', 
        questions: 2, 
        time: '15 phút', 
        mark: 'TW',
        type: 'writing'
      },

      // --- IELTS ---
      { 
        kind: 'IELTS', 
        skill: 'Listening', 
        title: 'IELTS Listening · Section 1: Form Completion', 
        detail: 'Điền thông tin đặt phòng khách sạn & du lịch', 
        questions: 4, 
        time: '7 phút', 
        mark: 'IL1',
        type: 'audio_mcq'
      },
      { 
        kind: 'IELTS', 
        skill: 'Reading', 
        title: 'IELTS Reading · Academic: Matching Headings', 
        detail: 'Nối tiêu đề bài nghiên cứu về biến đổi khí hậu', 
        questions: 4, 
        time: '10 phút', 
        mark: 'IR1',
        type: 'reading_passage'
      },
      { 
        kind: 'IELTS', 
        skill: 'Reading', 
        title: 'IELTS Reading · True / False / Not Given', 
        detail: 'Xác thực thông tin bài đọc lịch sử công nghệ', 
        questions: 4, 
        time: '8 phút', 
        mark: 'IR2',
        type: 'reading_passage'
      },
      { 
        kind: 'IELTS', 
        skill: 'Writing', 
        title: 'IELTS Writing · Task 2: Opinion Essay', 
        detail: 'Nghị luận xã hội: Giáo dục đại học và việc làm', 
        questions: 1, 
        time: '20 phút', 
        mark: 'IW2',
        type: 'writing'
      },
      { 
        kind: 'IELTS', 
        skill: 'Speaking', 
        title: 'IELTS Speaking · Part 2 & 3: Cue Card', 
        detail: 'Thuyết trình 2 phút về một vấn đề môi trường & thảo luận', 
        questions: 2, 
        time: '10 phút', 
        mark: 'IS2',
        type: 'speaking'
      }
    ];

    // Ngân hàng câu hỏi chi tiết cho từng đề thi
    const examDatabase = {
      'TOEIC Listening · Part 1: Photographs': {
        audioTitle: 'Audio Test Part 1 · Track 01 (Office & Warehouse)',
        audioScript: '[Narrator]: Look at the photo labeled number 1 in your test book. (A) The woman is filing paperwork into a cabinet. (B) The colleagues are reviewing architectural blueprints at a desk. (C) A presenter is speaking into a microphone. (D) The team members are adjusting their laptop monitors.',
        questions: [
          {
            text: 'Look at the image of the boardroom meeting. Which statement best describes the scene?',
            translated: 'Nhìn vào bức ảnh cuộc họp phòng hội đồng. Câu nào miêu tả đúng nhất khung cảnh?',
            choices: [
              'The woman is filing paperwork into a cabinet.',
              'The colleagues are reviewing architectural blueprints at a desk.',
              'A presenter is speaking into a microphone.',
              'The team members are adjusting their laptop monitors.'
            ],
            answer: 1,
            ai_explain: 'Đáp án B chính xác. Bức ảnh chụp các đồng nghiệp đang cùng xem bản vẽ thiết kế (architectural blueprints) trên mặt bàn. Các phương án A, C, D đều không có hành động tương ứng trong ảnh.'
          },
          {
            text: 'Look at the photo labeled number 2: A warehouse employee with clipboard.',
            translated: 'Nhìn vào bức ảnh số 2: Nhân viên nhà kho cầm bìa kẹp hồ sơ.',
            choices: [
              'He is operating heavy transport machinery.',
              'He is checking the inventory items on the shelves.',
              'He is packing goods inside a cardboard carton.',
              'He is sweeping the warehouse concrete corridor.'
            ],
            answer: 1,
            ai_explain: 'Đáp án B chính xác vì nhân viên đang kiểm tra danh mục hàng hóa (checking inventory items) trên các kệ hàng trong kho.'
          },
          {
            text: 'Photo number 3: A female barista serving customer.',
            translated: 'Bức ảnh số 3: Nhân viên pha chế nữ phục vụ khách hàng.',
            choices: [
              'She is handing a hot beverage cup across the service counter.',
              'She is wiping down the glass dining tables.',
              'She is baking fresh bread in a commercial oven.',
              'She is hanging a decorative sign on the coffee shop entrance.'
            ],
            answer: 0,
            ai_explain: 'Đáp án A chính xác (handing a beverage cup across the counter: đưa ly đồ uống qua quầy phục vụ).'
          },
          {
            text: 'Photo number 4: Construction workers wearing safety helmets.',
            translated: 'Bức ảnh số 4: Công nhân xây dựng đội mũ bảo hộ.',
            choices: [
              'They are dismantling scaffolding on the skyscraper facade.',
              'They are inspecting safety equipment at a construction site.',
              'They are painting exterior brick building walls.',
              'They are digging an excavation trench along the sidewalk.'
            ],
            answer: 1,
            ai_explain: 'Đáp án B đúng (inspecting safety equipment at a construction site: đang kiểm tra trang thiết bị an toàn).'
          }
        ]
      },

      'TOEIC Listening · Part 2: Question–Response': {
        audioTitle: 'Audio Test Part 2 · Track 02 (Questions 1 - 5)',
        audioScript: 'Q1: Where will the quarterly regional conference be held? (A) In the main convention auditorium. (B) Sometime around next Wednesday. (C) Yes, I registered yesterday.',
        questions: [
          {
            text: 'Where will the quarterly regional conference be held?',
            translated: 'Hội nghị khu vực quý này sẽ được tổ chức ở đâu?',
            choices: [
              'In the main convention auditorium.',
              'Sometime around next Wednesday afternoon.',
              'Yes, I submitted my online registration yesterday.'
            ],
            answer: 0,
            ai_explain: 'Câu hỏi hỏi về địa điểm "Where", đáp án A trả lời đúng địa điểm "In the main convention auditorium". B trả lời thời gian "When", C trả lời câu hỏi Yes/No.'
          },
          {
            text: 'Why hasn\'t the replacement printer cartridge arrived yet?',
            translated: 'Tại sao hộp mực máy in thay thế vẫn chưa được giao đến?',
            choices: [
              'I usually print twenty double-sided pages.',
              'There was a severe logistics delay at the supplier warehouse.',
              'Yes, the document has already been photocopied.'
            ],
            answer: 1,
            ai_explain: 'Câu hỏi hỏi nguyên nhân "Why", đáp án B giải thích lý do giao chậm do sự cố logistics của kho nhà cung cấp.'
          },
          {
            text: 'Would you mind reviewing my budget draft before I submit it?',
            translated: 'Bạn có phiền xem qua bản thảo ngân sách của tôi trước khi tôi nộp không?',
            choices: [
              'I would be happy to take a close look at it this afternoon.',
              'About twenty thousand dollars in total revenue.',
              'The accounting department submitted it last month.'
            ],
            answer: 0,
            ai_explain: '"Would you mind..." là lời nhờ vả lịch sự. Đáp án A đồng ý hỗ trợ xem qua vào buổi chiều.'
          },
          {
            text: 'Who was selected to head the overseas marketing initiative?',
            translated: 'Ai đã được chọn để phụ trách sáng kiến tiếp thị ở thị trường nước ngoài?',
            choices: [
              'The marketing brochure is being revised.',
              'Ms. Laura Jenkins from the Singapore branch office.',
              'We expanded our market share significantly.'
            ],
            answer: 1,
            ai_explain: 'Câu hỏi "Who" hỏi danh tính người phụ trách, đáp án B chỉ rõ cô Laura Jenkins từ chi nhánh Singapore.'
          },
          {
            text: 'Should we take the commuter express train or rent a car for the client visit?',
            translated: 'Chúng ta nên đi tàu cao tốc hay thuê xe ô tô để đi gặp khách hàng?',
            choices: [
              'The express train is much faster and avoids morning traffic.',
              'Yes, I visited the client earlier this morning.',
              'The rental fee was paid in cash.'
            ],
            answer: 0,
            ai_explain: 'Câu hỏi lựa chọn (A or B), đáp án A chọn phương án tàu cao tốc vì nhanh hơn và tránh kẹt xe.'
          }
        ]
      },

      'TOEIC Listening · Part 3: Short Conversations': {
        audioTitle: 'Audio Test Part 3 · Conversation: Contract Signing & Delivery',
        audioScript: '[Man]: Hi Sarah, have you heard back from the logistics firm about our overseas shipment? [Woman]: Yes, Mr. Tanaka just confirmed that the shipping containers will depart on Friday. However, we still need the legal department to sign the customs clearance agreement. [Man]: I will walk over to legal right away and ask director Miller to sign it before noon.',
        questions: [
          {
            text: 'What are the speakers mainly discussing?',
            translated: 'Những người nói chủ yếu thảo luận về vấn đề gì?',
            choices: [
              'Organizing an international training seminar',
              'The status of an overseas cargo shipment',
              'Interviewing candidates for the legal department',
              'Purchasing new industrial manufacturing containers'
            ],
            answer: 1,
            ai_explain: 'Hai nhân vật thảo luận về tiến độ lô hàng xuất khẩu ra nước ngoài (overseas cargo shipment).'
          },
          {
            text: 'What document is currently pending signature?',
            translated: 'Tài liệu nào hiện đang chờ chữ ký?',
            choices: [
              'The commercial customs clearance agreement',
              'The annual building lease renewal contract',
              'The quarterly vendor invoice receipt',
              'The employee non-disclosure agreement'
            ],
            answer: 0,
            ai_explain: 'Người phụ nữ nói rõ: "we still need the legal department to sign the customs clearance agreement" (hợp đồng thông quan hải quan).'
          },
          {
            text: 'What will the man do next?',
            translated: 'Người đàn ông sẽ làm gì tiếp theo?',
            choices: [
              'Call Mr. Tanaka to renegotiate shipping rates',
              'Visit the legal department to obtain a signature',
              'Inspect the shipping containers at the dock',
              'Send an email to the customs authority'
            ],
            answer: 1,
            ai_explain: 'Người đàn ông nói: "I will walk over to legal right away and ask director Miller to sign it" (đi sang phòng pháp chế để xin chữ ký).'
          }
        ]
      },

      'TOEIC Reading · Part 5: Incomplete Sentences': {
        questions: [
          {
            text: 'The newly appointed director implemented several initiatives aimed at _____ operating costs.',
            translated: 'Giám đốc mới được bổ nhiệm đã triển khai một số sáng kiến nhằm _____ chi phí vận hành.',
            choices: ['reduce', 'reduction', 'reducing', 'reducible'],
            answer: 2,
            ai_explain: 'Cụm từ "aimed at" đi kèm với V-ing (giới từ "at" + V-ing). Do đó "reducing" là đáp án chính xác.'
          },
          {
            text: 'Customers who experience unexpected connectivity errors should contact technical support _____.',
            translated: 'Khách hàng gặp sự cố kết nối bất ngờ nên liên hệ hỗ trợ kỹ thuật _____.',
            choices: ['prompt', 'promptly', 'promptness', 'prompting'],
            answer: 1,
            ai_explain: 'Cần một trạng từ (adverb) để bổ nghĩa cho động từ "contact". "Promptly" (nhanh chóng, ngay lập tức) là trạng từ duy nhất.'
          },
          {
            text: 'All expense reimbursement requests must be submitted _____ the last business day of the month.',
            translated: 'Tất cả các yêu cầu hoàn trả chi phí phải được gửi _____ ngày làm việc cuối cùng của tháng.',
            choices: ['by', 'between', 'during', 'among'],
            answer: 0,
            ai_explain: 'Giới từ "by" dùng với mốc thời gian cụ thể mang nghĩa "trước hoặc muộn nhất vào thời điểm đó". "By the last business day" là đúng chuẩn.'
          },
          {
            text: 'Although the initial market survey was inconclusive, the board members _____ approved the acquisition.',
            translated: 'Mặc dù cuộc khảo sát thị trường ban đầu chưa đưa ra kết luận rõ ràng, các thành viên hội đồng quản trị _____ đã thông qua thương vụ mua lại.',
            choices: ['nevertheless', 'despite', 'unless', 'whereas'],
            answer: 0,
            ai_explain: '"Nevertheless" (tuy nhiên, dẫu vậy) là trạng từ liên kết phù hợp logic ngữ nghĩa câu (mặc dù khảo sát chưa rõ ràng, dẫu vậy họ vẫn phê duyệt).'
          },
          {
            text: 'The warranty terms stipulate that replacement components will be provided free of charge, _____ shipping fees.',
            translated: 'Điều khoản bảo hành quy định rằng các linh kiện thay thế sẽ được cung cấp miễn phí, _____ phí vận chuyển.',
            choices: ['excluding', 'exclusion', 'exclusive', 'excluded'],
            answer: 0,
            ai_explain: '"Excluding" (ngoại trừ) đóng vai trò như giới từ đứng trước danh từ "shipping fees".'
          }
        ]
      },

      'TOEIC Reading · Part 6: Text Completion': {
        passageTitle: 'Internal Memorandum: IT Security Upgrade',
        passageText: 'To: All Staff Members\\nFrom: Systems Security Division\\nDate: October 12\\nSubject: Mandatory Network Credential Updates\\n\\nPlease be advised that our IT infrastructure will undergo an essential security upgrade this coming weekend. Starting Monday morning, all employees will be required to update their account passwords. Passwords must contain at least ten characters, including uppercase letters, numerals, and special characters. \\n\\n[1] _____ you experience difficulty logging into your workstation after the update, please contact the helpdesk directly. [2] _____. We appreciate your patience and cooperation as we strive to _____ our corporate data defenses.',
        questions: [
          {
            text: 'Choose the word that best fits blank [1]:',
            translated: 'Chọn từ phù hợp nhất cho chỗ trống [1]:',
            choices: ['Should', 'Unless', 'Despite', 'Because'],
            answer: 0,
            ai_explain: 'Cấu trúc đảo ngữ câu điều kiện loại 1: "Should you experience..." tương đương "If you experience..." (Nếu bạn gặp khó khăn...).'
          },
          {
            text: 'Choose the sentence that best fits blank [2]:',
            translated: 'Chọn câu phù hợp nhất cho chỗ trống [2]:',
            choices: [
              'Technical staff will be available on-site beginning at 7:30 A.M.',
              'The cafeteria menu has been revised for the upcoming quarter.',
              'All travel expense receipts should be delivered to accounting.',
              'The holiday party venue has been successfully reserved.'
            ],
            answer: 0,
            ai_explain: 'Đoạn văn đang nói về việc liên hệ bộ phận trợ giúp máy tính (helpdesk), nên câu hỗ trợ kỹ thuật có mặt từ 7:30 sáng là câu liên kết ý hợp lý nhất.'
          },
          {
            text: 'Choose the word that best fits blank [3]: "...strive to _____ our corporate data defenses."',
            translated: 'Chọn từ phù hợp nhất cho chỗ trống [3]:',
            choices: ['fortify', 'delay', 'neglect', 'disclose'],
            answer: 0,
            ai_explain: '"Fortify" mang nghĩa củng cố, tăng cường hệ thống phòng vệ dữ liệu công ty.'
          },
          {
            text: 'What is the primary objective of the memorandum?',
            translated: 'Mục đích chính của bản ghi nhớ là gì?',
            choices: [
              'To announce planned system downtime and password requirement changes',
              'To terminate redundant employee computer accounts',
              'To recruit senior software developers for the IT team',
              'To report an unauthorized data breach incident'
            ],
            answer: 0,
            ai_explain: 'Bản ghi nhớ thông báo về việc nâng cấp hệ thống và yêu cầu cập nhật mật khẩu mới.'
          }
        ]
      },

      'TOEIC Reading · Part 7: Reading Comprehension': {
        passageTitle: 'Business Inquiry & Product Catalog Notice',
        passageText: 'Dear Mr. Henderson,\\n\\nThank you for reaching out regarding Apex Furniture Solutions\\\' executive seating line. We have reviewed your custom order request for 60 ergonomically designed office chairs (Model AP-400X) for your upcoming headquarters expansion in Denver.\\n\\nBecause your order exceeds 50 units, your company qualifies for our wholesale corporate tier, which provides a 15% discount off the list price of $280 per chair. Additionally, we are pleased to offer complimentary ground delivery, provided the order is finalized before October 25.\\n\\nPlease confirm your preferred upholstery color (Charcoal Gray or Midnight Navy) by returning the attached purchase agreement signed by your procurement officer.\\n\\nSincerely,\\nEvelyn Vance\\nCorporate Sales Director, Apex Furniture',
        questions: [
          {
            text: 'Why did Ms. Vance write to Mr. Henderson?',
            translated: 'Tại sao cô Vance lại viết thư cho ông Henderson?',
            choices: [
              'To respond to an inquiry about an order of office chairs',
              'To advertise an upcoming clearance sale in Denver',
              'To request payment for an overdue furniture invoice',
              'To recruit a procurement officer for Apex Furniture'
            ],
            answer: 0,
            ai_explain: 'Đoạn đầu thư nêu rõ: "Thank you for reaching out regarding... executive seating line" (Phản hồi lại yêu cầu đặt hàng ghế văn phòng).'
          },
          {
            text: 'What special benefit is Mr. Henderson\'s company eligible for?',
            translated: 'Công ty của ông Henderson đủ điều kiện nhận ưu đãi đặc biệt nào?',
            choices: [
              'A 15% wholesale volume discount',
              'An extended five-year warranty package',
              'Free air express international shipping',
              'A complimentary sample conference table'
            ],
            answer: 0,
            ai_explain: 'Thư viết: "your company qualifies for our wholesale corporate tier, which provides a 15% discount".'
          },
          {
            text: 'What condition must be met to receive complimentary delivery?',
            translated: 'Điều kiện nào phải được đáp ứng để được miễn phí giao hàng?',
            choices: [
              'The order must be finalized before October 25.',
              'The chairs must be picked up directly at the Denver warehouse.',
              'Payment must be made exclusively via bank wire transfer.',
              'The purchase agreement must specify Midnight Navy color.'
            ],
            answer: 0,
            ai_explain: 'Thư nêu rõ: "provided the order is finalized before October 25" (miễn là đơn hàng hoàn tất trước ngày 25/10).'
          },
          {
            text: 'What is Mr. Henderson requested to do in order to confirm the purchase?',
            translated: 'Ông Henderson được yêu cầu làm gì để xác nhận đơn mua?',
            choices: [
              'Return the signed purchase agreement indicating the chosen color',
              'Schedule an in-person meeting with the regional sales representative',
              'Wire the full payment deposit to the Denver municipal bank',
              'Provide an estimate of next year\'s furniture requirements'
            ],
            answer: 0,
            ai_explain: 'Câu cuối thư: "confirm your preferred upholstery color... by returning the attached purchase agreement signed".'
          }
        ]
      },

      'TOEIC Speaking · Describe Picture & Opinion': {
        type: 'speaking',
        questions: [
          {
            text: 'Question 1: Describe a Picture\\nPrompt: Look at the photo showing a busy tech office collaboration space. Describe as many details as possible (people, activities, setting, ambiance).',
            translated: 'Câu 1: Miêu tả bức ảnh phòng làm việc công nghệ bận rộn. Nêu chi tiết người, hoạt động, bối cảnh.',
            prepTime: 45,
            speakTime: 45,
            sampleAnswer: 'This image captures a modern open-plan office environment. In the center, a group of four diverse colleagues are gathered around a standing conference table, actively examining a colorful digital layout on a large tablet. To the left, large floor-to-ceiling windows illuminate the workspace with natural sunlight. The overall atmosphere appears dynamic, collaborative, and highly focused.',
            ai_explain: 'Tiêu chí chấm TOEIC Speaking: Phát âm chuẩn xác (Pronunciation), ngữ điệu tự nhiên (Intonation), vốn từ vựng phong phú (Vocabulary), và ngữ pháp liền mạch (Grammar accuracy).'
          },
          {
            text: 'Question 2: Express an Opinion\\nPrompt: Do you agree or disagree that allowing employees to work remotely increases overall company productivity? Give reasons and specific examples.',
            translated: 'Câu 2: Nêu quan điểm. Bạn đồng ý hay không đồng ý rằng làm việc từ xa giúp tăng năng suất công ty? Đưa lý do và ví dụ.',
            prepTime: 30,
            speakTime: 60,
            sampleAnswer: 'In my opinion, I strongly agree that remote work enhances overall employee productivity. Firstly, eliminating long daily commutes saves employees substantial energy and reduces morning stress, allowing them to start their workday refreshed. Secondly, working in a personalized home setting significantly minimizes office distractions, facilitating deep, uninterrupted focus. For example, in my previous software firm, team output increased by 20% after implementing flexible hybrid schedules.',
            ai_explain: 'Cần có quan điểm rõ ràng (Clear thesis), tối thiểu 2 luận điểm hỗ trợ mạnh mẽ (Supporting arguments), và ví dụ thực tế thuyết phục.'
          }
        ]
      },

      'TOEIC Writing · Email Reply & Opinion Essay': {
        type: 'writing',
        questions: [
          {
            text: 'Task 1: Respond to a Customer Inquiry Email\\nDirections: Read the email from a customer complaining about a damaged product delivery. Write a professional reply of 80-120 words offering an apology, an explanation, and two concrete solutions (replacement or refund).',
            translated: 'Bài 1: Trả lời email khiếu nại của khách hàng về kiện hàng bị hư hại. Viết thư phản hồi 80-120 từ xin lỗi và đưa ra 2 hướng xử lý.',
            minWords: 80,
            sampleAnswer: 'Dear Mr. Davis,\\n\\nThank you for bringing this issue to our attention. We sincerely apologize for the inconvenience caused by the damaged delivery of your porcelain tableware set.\\n\\nQuality assurance is our highest priority, and we have already initiated an investigation with our logistics carrier to prevent future occurrences. To resolve this matter immediately, we would be delighted to either dispatch an express replacement set to your address at no additional charge, or process a full refund to your original payment card within 24 hours.\\n\\nPlease let us know your preferred resolution.\\n\\nSincerely,\\nCustomer Support Team',
            ai_explain: 'Tiêu chí TOEIC Writing Email: Văn phong lịch sự, giải quyết đầy đủ các yêu cầu của đề bài, cấu trúc câu chặt chẽ và không có lỗi ngữ pháp cơ bản.'
          },
          {
            text: 'Task 2: Write an Opinion Essay (minimum 200 words)\\nDirections: Some companies believe that team members should strictly dress in formal business attire, while others encourage casual clothing. Which approach do you support, and why?',
            translated: 'Bài 2: Viết luận nêu quan điểm (tối thiểu 200 từ) về trang phục công sở: Trang trọng (Formal) hay Thoải mái (Casual)?',
            minWords: 200,
            sampleAnswer: 'In modern corporate cultures, the debate surrounding office dress codes has gained widespread attention. While traditional perspectives advocate for strict business formal attire to preserve professionalism, I firmly believe that adopting a smart-casual dress code is vastly superior for employee satisfaction and creative performance.\\n\\nFirst and foremost, comfortable clothing directly promotes psychological well-being. When individuals are liberated from rigid suits and ties, they experience lower physical fatigue throughout long working hours, which consequently enhances cognitive efficiency and problem-solving agility. Numerous leading technology enterprises, such as Google and Apple, have long demonstrated that casual atmospheres stimulate groundbreaking innovation without undermining professional rigor.\\n\\nFurthermore, casual dress codes break down unnecessary hierarchical barriers among coworkers. In an open environment where junior staff and executives wear similar relaxed attire, team members feel more empowered to voice unconventional ideas during brainstorming sessions.\\n\\nIn conclusion, while formal dress remains appropriate for courtroom settings or diplomatic banquets, everyday office environments thrive most when prioritizing comfort and authentic collaboration.',
            ai_explain: 'Tiêu chí TOEIC Writing Essay: Cấu trúc 4 đoạn (Mở bài, 2 Thân bài, Kết luận), liên kết mạch lạc (Coherence), vốn từ học thuật phong phú.'
          }
        ]
      },

      'IELTS Listening · Section 1: Form Completion': {
        audioTitle: 'IELTS Listening Section 1 · Oceanic Hotel Conference Booking',
        audioScript: '[Receptionist]: Good morning, Oceanic Conference Suites. How can I help you today? [Customer]: Hello, I would like to book a conference room for our annual medical seminar next month. [Receptionist]: Certainly sir. May I take your full name? [Customer]: Yes, it is Dr. Arthur Pendelton. That is P-E-N-D-E-L-T-O-N. [Receptionist]: And the expected date of arrival? [Customer]: We plan to arrive on the fourteenth of November and depart on the seventeenth.',
        questions: [
          {
            text: 'Question 1: What is the correct spelling of the client\'s family name?',
            translated: 'Họ của khách hàng được đánh vần chính xác như thế nào?',
            choices: ['PENDELTON', 'PEMBERTON', 'PENNINGTON', 'PENDLEBURY'],
            answer: 0,
            ai_explain: 'Đoạn băng đánh vần rõ ràng: P-E-N-D-E-L-T-O-N.'
          },
          {
            text: 'Question 2: What is the purpose of the reservation?',
            translated: 'Mục đích của việc đặt phòng là gì?',
            choices: [
              'An annual medical research seminar',
              'A family wedding anniversary celebration',
              'A regional tennis championship banquet',
              'An art exhibition gallery opening'
            ],
            answer: 0,
            ai_explain: 'Khách hàng nói: "book a conference room for our annual medical seminar".'
          },
          {
            text: 'Question 3: What is the scheduled arrival date?',
            translated: 'Ngày đến dự kiến là ngày nào?',
            choices: [
              '14th of November',
              '17th of November',
              '4th of November',
              '21st of November'
            ],
            answer: 0,
            ai_explain: 'Khách hàng nói: "arrive on the fourteenth of November" (14 tháng 11).'
          },
          {
            text: 'Question 4: What special catering requirement did the doctor mention?',
            translated: 'Yêu cầu phục vụ đồ ăn đặc biệt nào được nhắc tới?',
            choices: [
              'Vegetarian and gluten-free dietary options',
              'Traditional three-course French cuisine',
              'Barbecue buffet served on the outdoor terrace',
              'All meals must be served without seafood'
            ],
            answer: 0,
            ai_explain: 'Trong hội thảo y khoa, khách hàng yêu cầu thực đơn ăn chay và không chứa gluten.'
          }
        ]
      },

      'IELTS Reading · Academic: Matching Headings': {
        passageTitle: 'The Architecture of Ancient Aqueducts',
        passageText: 'Paragraph A: The engineering prowess of the Roman Empire remains most visible through its monumental aqueduct systems. Spanning hundreds of kilometers across rugged topography, these gravity-fed waterways delivered thousands of cubic meters of fresh potable water to urban metropolises daily.\\n\\nParagraph B: The foundational principle of aqueduct design relied on a gentle, consistent downward gradient. If the decline was too steep, the rushing water would erode stone joints and rupture pipes; if too shallow, the current would stagnate and accumulate sediment.\\n\\nParagraph C: While stone archways are the iconic image of Roman water systems, arched bridges accounted for less than twenty percent of the total distance. The overwhelming majority of the conduit network was constructed underground, shielded from contamination, seasonal evaporation, and hostile military sabotage.',
        questions: [
          {
            text: 'Which heading best fits Paragraph A?',
            translated: 'Tiêu đề nào phù hợp nhất với Đoạn A?',
            choices: [
              'A monumental feat of imperial civil engineering',
              'The catastrophic decline of urban Roman populations',
              'Chemical purification techniques in ancient cisterns',
              'The financial collapse of public infrastructure'
            ],
            answer: 0,
            ai_explain: 'Đoạn A ca ngợi tài năng kỹ thuật xây dựng công trình vĩ đại của đế chế La Mã (engineering prowess, monumental aqueduct systems).'
          },
          {
            text: 'Which heading best fits Paragraph B?',
            translated: 'Tiêu đề nào phù hợp nhất với Đoạn B?',
            choices: [
              'The delicate balance of gravitational gradient calculations',
              'The extraction of raw volcanic marble materials',
              'Religious rituals dedicated to freshwater springs',
              'Military defense strategies along border provinces'
            ],
            answer: 0,
            ai_explain: 'Đoạn B giải thích việc tính toán độ dốc trọng lực (gravitational gradient) vừa đủ để nước chảy mà không làm vỡ ống hay đọng cặn.'
          },
          {
            text: 'Which heading best fits Paragraph C?',
            translated: 'Tiêu đề nào phù hợp nhất với Đoạn C?',
            choices: [
              'The predominance and defensive utility of subterranean conduits',
              'Architectural flaws of monumental stone archways',
              'The seasonal fluctuation of Mediterranean rivers',
              'The modern demolition of historic Roman bridges'
            ],
            answer: 0,
            ai_explain: 'Đoạn C giải thích phần lớn đường ống nằm ngầm dưới lòng đất (subterranean conduits: hơn 80%) để bảo vệ nguồn nước khỏi bay hơi và quân địch.'
          },
          {
            text: 'According to the passage, why were most aqueduct segments built below ground?',
            translated: 'Theo bài đọc, tại sao hầu hết các đoạn cống dẫn nước được xây dưới lòng đất?',
            choices: [
              'To guard against contamination, evaporation, and sabotage',
              'Because stone quarries had exhausted their marble reserves',
              'To avoid paying municipal urban property taxes',
              'Because Roman law prohibited above-ground stone bridges'
            ],
            answer: 0,
            ai_explain: 'Đoạn C chỉ rõ: "shielded from contamination, seasonal evaporation, and hostile military sabotage".'
          }
        ]
      },

      'IELTS Reading · True / False / Not Given': {
        passageTitle: 'Artificial Intelligence in Modern Healthcare',
        passageText: 'Recent breakthroughs in deep convolutional neural networks have accelerated the deployment of artificial intelligence across clinical diagnostics. In a landmark 2023 international clinical trial, an AI algorithm trained on more than 100,000 mammograms demonstrated a diagnostic accuracy matching senior board-certified radiologists in identifying early-stage malignant tumors. Crucially, the automated system reduced false positive diagnoses by approximately 5.7 percent, significantly decreasing unnecessary patient biopsies. However, medical ethicists emphasize that automated tools should assist, rather than replace, human practitioners.',
        questions: [
          {
            text: 'Statement 1: The AI algorithm analyzed more than one hundred thousand diagnostic scans during its training.',
            translated: 'Khẳng định 1: Thuật toán AI đã phân tích hơn 100.000 bản chụp chẩn đoán trong giai đoạn huấn luyện.',
            choices: ['TRUE', 'FALSE', 'NOT GIVEN'],
            answer: 0,
            ai_explain: 'Bài đọc nêu rõ: "trained on more than 100,000 mammograms". Do đó là TRUE.'
          },
          {
            text: 'Statement 2: The artificial intelligence system completely outperformed all human doctors in detecting all known illnesses.',
            translated: 'Khẳng định 2: Hệ thống AI vượt trội hoàn toàn tất cả các bác sĩ trong việc phát hiện mọi bệnh tật.',
            choices: ['TRUE', 'FALSE', 'NOT GIVEN'],
            answer: 1,
            ai_explain: 'Bài đọc chỉ nói AI đạt độ chính xác tương đương (matching) các bác sĩ X-quang kỳ cựu trong việc phát hiện khối u ác tính sớm, không hề vượt trội mọi bệnh. Do đó là FALSE.'
          },
          {
            text: 'Statement 3: False positive diagnoses were reduced by more than fifteen percent.',
            translated: 'Khẳng định 3: Các chẩn đoán dương tính giả đã giảm hơn 15%.',
            choices: ['TRUE', 'FALSE', 'NOT GIVEN'],
            answer: 1,
            ai_explain: 'Bài đọc viết giảm khoảng 5.7%, không phải hơn 15%. Do đó là FALSE.'
          },
          {
            text: 'Statement 4: The developers of the AI algorithm plan to launch a commercial smartphone application next year.',
            translated: 'Khẳng định 4: Nhóm phát triển thuật toán dự định ra mắt ứng dụng điện thoại thương mại vào năm sau.',
            choices: ['TRUE', 'FALSE', 'NOT GIVEN'],
            answer: 2,
            ai_explain: 'Bài đọc không hề đề cập đến ứng dụng điện thoại (smartphone app) hay kế hoạch năm sau. Do đó là NOT GIVEN.'
          }
        ]
      },

      'IELTS Writing · Task 2: Opinion Essay': {
        type: 'writing',
        questions: [
          {
            text: 'Writing Task 2: Essay Prompt\\nDirections: Some people argue that technological advancements in automation and artificial intelligence will inevitably lead to widespread unemployment, while others believe that technology creates more meaningful job opportunities than it destroys.\\n\\nDiscuss both views and give your own reasoned opinion. Write at least 250 words.',
            translated: 'IELTS Writing Task 2: Tranh luận về tác động của AI/Tự động hóa đến việc làm. Thảo luận cả 2 quan điểm và nêu ý kiến bản thân (tối thiểu 250 từ).',
            minWords: 250,
            sampleAnswer: 'The exponential acceleration of artificial intelligence and robotic automation has ignited profound socioeconomic debates regarding the future of human labor. While a substantial demographic fears that mechanized efficiency will trigger systemic technological unemployment, I contend that innovation historically displaces routine manual labor while spawning far richer, intellectually stimulating vocations.\\n\\nOn the one hand, apprehension regarding job obsolescence is undeniably justified in the short term. Repetitive cognitive and physical tasks, such as factory assembly, basic bookkeeping, and customer service telephone routing, can now be executed by algorithms with unprecedented speed and zero fatigue. Consequently, vulnerable workforces lacking access to technical retraining face genuine risks of economic marginalization. For example, the automation of automated toll booths and self-checkout kiosks has visibly reduced entry-level clerical employment worldwide.\\n\\nOn the other hand, technological revolutions have historically catalyzed net employment expansion rather than permanent deprivation. When routine tasks are automated, overall productivity surges and operational overhead declines, releasing capital for investment into novel industries. Emerging domains such as renewable energy grid management, bioinformatic engineering, cybernetic defense, and creative content architecture did not exist three decades ago. Furthermore, machines fundamentally lack empathy, nuanced ethical discernment, and complex artistic intuition—qualities that will remain distinctly human advantages in education, psychological counseling, and strategic leadership.\\n\\nIn conclusion, while the transition period necessitates proactive governmental investment into adult digital literacy and vocational reskilling, artificial intelligence should be recognized not as an economic destroyer, but as a transformative tool that elevates human potential.',
            ai_explain: 'Tiêu chí chấm IELTS Writing Task 2 (Band 1.0 - 9.0):\\n1. Task Achievement (Giải quyết trọn vẹn cả 2 quan điểm)\\n2. Coherence and Cohesion (Liên kết mạch lạc giữa các đoạn)\\n3. Lexical Resource (Từ vựng học thuật C1/C2 phong phú)\\n4. Grammatical Range and Accuracy (Đa dạng cấu trúc câu phức/ghép, không lỗi ngữ pháp).'
          }
        ]
      },

      'IELTS Speaking · Part 2 & 3: Cue Card': {
        type: 'speaking',
        questions: [
          {
            text: 'IELTS Speaking Part 2: Cue Card\\nDescribe an environmental problem that your country or community is facing.\\nYou should say:\\n- What the problem is and how severe it is\\n- What causes this problem\\n- How it impacts people\'s everyday lives\\nAnd explain what measures can be taken to solve or mitigate it.',
            translated: 'IELTS Speaking Part 2: Thuyết trình 2 phút miêu tả một vấn đề môi trường mà cộng đồng của bạn đang đối mặt, nguyên nhân, ảnh hưởng và giải pháp.',
            prepTime: 60,
            speakTime: 120,
            sampleAnswer: 'I would like to talk about the escalating issue of urban air pollution and particulate smog in major metropolitan areas in Vietnam. Over the past decade, rapid industrialization paired with an overwhelming density of private gasoline motorbikes has significantly degraded ambient air quality.\\n\\nThe primary drivers behind this crisis are twofold: emissions from heavy vehicular traffic during morning rush hours, and unregulated construction dust from rapid urban development. On days when hazardous PM2.5 levels spike, residents experience respiratory ailments, eye irritation, and long-term cardiovascular risks.\\n\\nTo combat this pressing crisis, municipalities must expand clean public transit networks, incentivize electric two-wheelers, and enforce strict dust-suppression regulations on commercial builders. Public awareness campaigns also play a crucial role in encouraging greener lifestyle habits.',
            ai_explain: 'Tiêu chí chấm IELTS Speaking: Fluency & Coherence (Độ lưu loát và mạch lạc), Lexical Resource (Vốn từ theo chủ đề môi trường), Grammatical Range (Cấu trúc ngữ pháp), Pronunciation (Phát âm và ngữ điệu tự nhiên).'
          },
          {
            text: 'IELTS Speaking Part 3: Two-way Discussion\\nDiscussion Question: Do you believe international treaties or individual consumer actions are more effective in curbing global carbon emissions?',
            translated: 'IELTS Speaking Part 3: Bạn nghĩ hiệp ước quốc tế hay hành động của từng người tiêu dùng hiệu quả hơn trong việc cắt giảm khí thải toàn cầu?',
            prepTime: 15,
            speakTime: 60,
            sampleAnswer: 'In my perspective, while individual lifestyle modifications like reducing single-use plastics are commendable, legally binding international treaties wield vastly superior influence. Global agreements compel national governments to legislate carbon tax frameworks, mandate industrial emission ceilings, and redirect billions of subsidies toward green renewable infrastructure. Without macro-level institutional mandates, grassroots consumer efforts simply cannot operate at the scale required to mitigate global climate change.',
            ai_explain: 'Cần phân tích đa chiều (Macro vs Micro), dùng từ vựng học thuật (legally binding, institutional mandates, grassroots efforts).'
          }
        ]
      }
    };

    // ==========================================
    // 2. SCORING ENGINES: TOEIC (10-990) & IELTS (1.0-9.0)
    // ==========================================
    function calculateToeicScore(correct, total, skill) {
        const ratio = total > 0 ? (correct / total) : 0;
        let scaledScore = 0;
        if (skill === 'Listening') {
            scaledScore = Math.round(5 + ratio * 490);
            scaledScore = Math.min(495, Math.max(5, Math.round(scaledScore / 5) * 5));
        } else if (skill === 'Reading') {
            scaledScore = Math.round(5 + ratio * 490);
            scaledScore = Math.min(495, Math.max(5, Math.round(scaledScore / 5) * 5));
        } else {
            // Speaking & Writing (thang 200)
            scaledScore = Math.round(ratio * 200);
            scaledScore = Math.min(200, Math.max(10, Math.round(scaledScore / 10) * 10));
        }

        let cefr = 'A1';
        if (scaledScore >= 400 || (skill !== 'Listening' && skill !== 'Reading' && scaledScore >= 160)) cefr = 'C1 (Advanced)';
        else if (scaledScore >= 300 || scaledScore >= 120) cefr = 'B2 (Upper-Intermediate)';
        else if (scaledScore >= 200 || scaledScore >= 80) cefr = 'B1 (Intermediate)';
        else cefr = 'A2 (Elementary)';

        return {
            scaledScore: scaledScore,
            maxScore: (skill === 'Listening' || skill === 'Reading') ? 495 : 200,
            cefr: cefr,
            display: `${scaledScore} pts (${cefr})`
        };
    }

    function calculateIeltsBand(correct, total, skill) {
        const ratio = total > 0 ? (correct / total) : 0;
        let band = 1.0;
        if (ratio >= 0.90) band = 8.5;
        else if (ratio >= 0.80) band = 7.5;
        else if (ratio >= 0.70) band = 7.0;
        else if (ratio >= 0.60) band = 6.5;
        else if (ratio >= 0.50) band = 6.0;
        else if (ratio >= 0.40) band = 5.5;
        else if (ratio >= 0.30) band = 5.0;
        else band = 4.0;

        let badge = 'Competent User';
        if (band >= 8.0) badge = 'Very Good / Expert User';
        else if (band >= 7.0) badge = 'Good User';
        else if (band >= 6.0) badge = 'Competent User';
        else badge = 'Modest User';

        return {
            band: band.toFixed(1),
            badge: badge,
            display: `Band ${band.toFixed(1)} · ${badge}`
        };
    }

    // ==========================================
    // 3. BOOKMARK & REPORT SYSTEM
    // ==========================================
    function getBookmarks() {
        return JSON.parse(localStorage.getItem('lingua-bookmarks') || '[]');
    }

    function getReports() {
        return JSON.parse(localStorage.getItem('lingua-reports') || '[]');
    }

    function isQuestionBookmarked(title, qIndex) {
        const list = getBookmarks();
        return list.some(b => b.title === title && b.qIndex === qIndex);
    }

    function toggleBookmark(title, qIndex) {
        let list = getBookmarks();
        const existingIdx = list.findIndex(b => b.title === title && b.qIndex === qIndex);
        
        if (existingIdx !== -1) {
            list.splice(existingIdx, 1);
            localStorage.setItem('lingua-bookmarks', JSON.stringify(list));
            notify('Đã xóa câu hỏi khỏi sổ tay lưu trữ.');
        } else {
            const exam = examDatabase[title] || { questions: questions };
            const q = exam.questions[qIndex];
            list.unshift({
                id: 'bm_' + Date.now(),
                title: title,
                qIndex: qIndex,
                date: new Date().toISOString(),
                questionText: q.text,
                translated: q.translated,
                choices: q.choices,
                answer: q.answer,
                ai_explain: q.ai_explain
            });
            localStorage.setItem('lingua-bookmarks', JSON.stringify(list));
            notify('⭐ Đã lưu câu hỏi vào Sổ tay!');
        }
        
        renderQuestion();
        renderBookmarksView();
    }

    let activeReportingContext = null;
    function openReportModal(title, qIndex) {
        activeReportingContext = { title, qIndex };
        $('#report-q-index').value = qIndex;
        $('#report-modal').classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeReportModal() {
        $('#report-modal').classList.remove('open');
        document.body.style.overflow = '';
        activeReportingContext = null;
    }

    function submitReport(e) {
        e.preventDefault();
        if (!activeReportingContext) return;
        
        const selectedReason = $('input[name="report_reason"]:checked')?.value || 'Khác';
        const note = $('#report-note').value.trim();
        const { title, qIndex } = activeReportingContext;
        const exam = examDatabase[title] || { questions: questions };
        const q = exam.questions[qIndex] || {};

        const reports = getReports();
        reports.unshift({
            id: 'rep_' + Date.now(),
            title: title,
            qIndex: qIndex,
            date: new Date().toISOString(),
            reason: selectedReason,
            note: note,
            questionText: q.text || 'Câu hỏi',
            status: 'Đã tiếp nhận'
        });
        localStorage.setItem('lingua-reports', JSON.stringify(reports));

        closeReportModal();
        notify('🚩 Cảm ơn bạn! Báo cáo đã được ghi nhận.');
        renderBookmarksView();
        renderQuestion();
    }

    function switchBookmarkTab(tab) {
        if (tab === 'bookmarks') {
            $('#tab-btn-bookmarks').classList.add('active');
            $('#tab-btn-reports').classList.remove('active');
            $('#tab-content-bookmarks').style.display = 'block';
            $('#tab-content-reports').style.display = 'none';
        } else {
            $('#tab-btn-bookmarks').classList.remove('active');
            $('#tab-btn-reports').classList.add('active');
            $('#tab-content-bookmarks').style.display = 'none';
            $('#tab-content-reports').style.display = 'block';
        }
    }

    function renderBookmarksView() {
        const bookmarks = getBookmarks();
        const reports = getReports();

        if ($('#count-bookmarks')) $('#count-bookmarks').textContent = bookmarks.length;
        if ($('#count-reports')) $('#count-reports').textContent = reports.length;

        // Render Bookmarks
        const bList = $('#bookmarks-list');
        if (bList) {
            if (bookmarks.length === 0) {
                bList.innerHTML = `<div class="empty-state" style="padding:40px; text-align:center; background:#fff; border-radius:12px; border:1px solid var(--line);">
                   <div style="font-size:32px; margin-bottom:8px;">⭐</div>
                   <h3 style="margin:0 0 4px;">Chưa có câu hỏi nào được lưu</h3>
                   <p style="color:var(--muted); font-size:13px;">Trong lúc làm bài thi, bấm "Lưu câu" để xem lại những câu hỏi cần nhớ nhé.</p>
                </div>`;
            } else {
                bList.innerHTML = bookmarks.map((b, i) => `
                    <div class="bookmark-card">
                       <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                          <div>
                             <span class="skill-pill reading" style="font-size:10px;">${b.title}</span>
                             <span style="font-size:11px; color:var(--muted); margin-left:8px;">Câu ${b.qIndex + 1}</span>
                          </div>
                          <button class="text-button" style="color:#ef4444; font-size:12px;" onclick="removeBookmark('${b.title}', ${b.qIndex})">Xóa</button>
                       </div>
                       <h4 style="margin:0 0 6px; font-size:14px; line-height:1.5;">${b.questionText}</h4>
                       <p style="margin:0 0 10px; font-size:12px; color:var(--muted); font-style:italic;">${b.translated || ''}</p>
                       <div style="background:#f8fafc; border-radius:8px; padding:10px 12px; font-size:12.5px; line-height:1.6; border-left:3px solid var(--green);">
                          <strong>Đáp án đúng:</strong> ${b.choices ? b.choices[b.answer] : 'N/A'}<br>
                          <span style="color:#475569;">${b.ai_explain || ''}</span>
                       </div>
                    </div>
                `).join('');
            }
        }

        // Render Reports
        const rList = $('#reports-list');
        if (rList) {
            if (reports.length === 0) {
                rList.innerHTML = `<div class="empty-state" style="padding:40px; text-align:center; background:#fff; border-radius:12px; border:1px solid var(--line);">
                   <div style="font-size:32px; margin-bottom:8px;">🚩</div>
                   <h3 style="margin:0 0 4px;">Chưa có báo cáo nào</h3>
                   <p style="color:var(--muted); font-size:13px;">Nếu phát hiện lỗi ngữ pháp hay đáp án chưa chuẩn, bạn hãy báo cáo để Lingua hoàn thiện hơn.</p>
                </div>`;
            } else {
                rList.innerHTML = reports.map((r, i) => `
                    <div class="bookmark-card" style="border-left:4px solid #ef4444;">
                       <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                          <strong style="color:#ef4444; font-size:13px;">🚩 ${r.reason}</strong>
                          <span class="skill-pill" style="background:#fef2f2; color:#b91c1c;">${r.status}</span>
                       </div>
                       <p style="margin:0 0 6px; font-size:12px; color:var(--muted);">${r.title} · Câu ${r.qIndex + 1} · ${new Date(r.date).toLocaleDateString('vi-VN')}</p>
                       <p style="margin:0 0 8px; font-size:13.5px; font-weight:600;">"${r.questionText.slice(0, 100)}..."</p>
                       ${r.note ? `<p style="margin:0; font-size:12px; background:#fff; border:1px solid var(--line); padding:6px 10px; border-radius:6px; color:#334155;"><strong>Ghi chú của bạn:</strong> ${r.note}</p>` : ''}
                    </div>
                `).join('');
            }
        }
    }

    function removeBookmark(title, qIndex) {
        toggleBookmark(title, qIndex);
    }

    // ==========================================
    // 4. USER PROFILE & TARGETS
    // ==========================================
    function getUserProfile() {
        const stored = localStorage.getItem('lingua-profile');
        if (stored) return JSON.parse(stored);
        
        const username = localStorage.getItem('lingua-user') || 'Minh Anh';
        return {
            name: username,
            email: username.includes('@') ? username : `${username.toLowerCase().replace(/\\s+/g, '')}@lingua.edu.vn`,
            targetExam: 'TOEIC 750+',
            targetDate: new Date(Date.now() + 45 * 24 * 3600 * 1000).toISOString().split('T')[0]
        };
    }

    function saveUserProfile(profile) {
        localStorage.setItem('lingua-profile', JSON.stringify(profile));
        localStorage.setItem('lingua-user', profile.name);
        showApp(profile.name);
        renderProfileView();
        notify('Cập nhật hồ sơ & mục tiêu thành công!');
    }

    function renderProfileView() {
        const profile = getUserProfile();
        
        if ($('#profile-display-name')) $('#profile-display-name').textContent = profile.name;
        if ($('#profile-email')) $('#profile-email').textContent = profile.email;
        if ($('#profile-target-title')) $('#profile-target-title').textContent = profile.targetExam;
        
        const initials = profile.name.trim().split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase() || 'MA';
        if ($('#profile-big-avatar')) $('#profile-big-avatar').textContent = initials;
        
        // Countdown
        if (profile.targetDate && $('#profile-countdown')) {
            const diff = Math.ceil((new Date(profile.targetDate) - new Date()) / (1000 * 3600 * 24));
            $('#profile-countdown').textContent = diff > 0 ? `Còn ${diff} ngày tới ngày thi` : 'Đã đến ngày thi!';
        }

        // Fill form fields
        if ($('#edit-profile-name')) $('#edit-profile-name').value = profile.name;
        if ($('#edit-profile-exam')) $('#edit-profile-exam').value = profile.targetExam;
        if ($('#edit-profile-date')) $('#edit-profile-date').value = profile.targetDate || '';

        // Calculate skill stats from real history
        const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
        const stats = { Listening: { correct: 0, total: 0 }, Reading: { correct: 0, total: 0 }, Writing: { correct: 0, total: 0 }, Speaking: { correct: 0, total: 0 } };
        
        history.forEach(item => {
            const skill = item.skill || (item.title.includes('Listening') ? 'Listening' : (item.title.includes('Reading') ? 'Reading' : (item.title.includes('Writing') ? 'Writing' : 'Speaking')));
            if (stats[skill]) {
                stats[skill].correct += (item.correct || 0);
                stats[skill].total += (item.total || 1);
            }
        });

        for (const [sk, data] of Object.entries(stats)) {
            const percent = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 70;
            const bar = $(`#bar-${sk.toLowerCase()}`);
            const val = $(`#val-${sk.toLowerCase()}`);
            if (bar) bar.style.width = `${percent}%`;
            if (val) val.textContent = `${percent}%`;
        }
    }

    $('#profile-edit-form')?.addEventListener('submit', (e) => {
        e.preventDefault();
        const updated = {
            name: $('#edit-profile-name').value.trim(),
            email: $('#profile-email').textContent,
            targetExam: $('#edit-profile-exam').value,
            targetDate: $('#edit-profile-date').value
        };
        saveUserProfile(updated);
    });

    function resetUserData() {
        if (!confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử thi và câu hỏi đã lưu?')) return;
        localStorage.removeItem('lingua-history');
        localStorage.removeItem('lingua-bookmarks');
        localStorage.removeItem('lingua-reports');
        notify('Đã đặt lại dữ liệu học tập.');
        updateScores();
        renderBookmarksView();
        renderProfileView();
    }

    // ==========================================
    // 5. EXAM EXECUTION & RUNTIME
    // ==========================================
    let currentExamData = null;
    let currentExamTitle = '';
    let currentQuestions = [];
    let isReviewMode = false;
    let simulatedAudioPlaying = false;
    let audioTimer = null;
    let audioProgressVal = 0;
    let isSpeakingRecording = false;

    function openExam(title) {
        currentExamTitle = title;
        isReviewMode = false;
        
        const courseConfig = courses.find(c => c.title === title) || { kind: 'TOEIC', skill: 'Reading', time: '15 phút' };
        currentExamData = examDatabase[title] || { questions: questions };
        currentQuestions = currentExamData.questions || questions;

        questionIndex = 0;
        correctAnswers = 0;
        userAnswers = new Array(currentQuestions.length).fill(null);
        
        $('#exam-label').textContent = title;
        $('#exam-backdrop').classList.add('open');
        document.body.style.overflow = 'hidden';

        const parseMinutes = parseInt(courseConfig.time) || 15;
        
        $('#exam-content').innerHTML = `
          <div class="exam-layout">
             <div class="exam-main" id="exam-main-area"></div>
             <div class="exam-sidebar">
                <div class="exam-timer">
                   <div class="timer-clock" id="timer-clock">${String(parseMinutes).padStart(2,'0')}:00</div>
                   <div class="timer-label">Thời gian còn lại</div>
                </div>
                <div style="margin-top: 10px;">
                   <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                      <span style="font-size:11px; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.5px;">Danh sách câu</span>
                      <span class="skill-pill ${courseConfig.skill.toLowerCase()}">${courseConfig.skill}</span>
                   </div>
                   <div class="question-grid" id="question-grid"></div>
                </div>
                <button class="primary" style="margin-top: auto; padding: 12px; text-align: center; justify-content: center; width: 100%; display: flex;" id="submit-exam-btn">Nộp bài sớm</button>
             </div>
          </div>
        `;
        
        renderQuestionGrid();
        renderQuestion();
        startTimer(parseMinutes);
        
        $('#submit-exam-btn').addEventListener('click', finishExam);
        $('#close-modal').focus();
    }

    function renderQuestionGrid() {
        const grid = $('#question-grid');
        if (!grid) return;
        grid.innerHTML = currentQuestions.map((_, i) => `
            <button class="q-btn ${i === questionIndex ? 'active' : ''} ${userAnswers[i] !== null ? 'answered' : ''}" data-qindex="${i}">
               ${i + 1}
            </button>
        `).join('');
        $$('.q-btn').forEach(btn => btn.addEventListener('click', () => {
            questionIndex = Number(btn.dataset.qindex);
            renderQuestion();
            renderQuestionGrid();
        }));
    }

    function renderQuestion() {
        const item = currentQuestions[questionIndex];
        const hasAnswered = userAnswers[questionIndex] !== null;
        const uAns = userAnswers[questionIndex];
        const isBookmarked = isQuestionBookmarked(currentExamTitle, questionIndex);
        
        let headerHtml = `
          <div class="q-action-bar">
             <div class="q-action-btns">
                <button class="q-tool-btn ${isBookmarked ? 'bookmarked' : ''}" onclick="toggleBookmark('${currentExamTitle}', ${questionIndex})">
                   <span>${isBookmarked ? '★' : '☆'}</span> ${isBookmarked ? 'Đã lưu' : 'Lưu câu'}
                </button>
                <button class="q-tool-btn" onclick="openReportModal('${currentExamTitle}', ${questionIndex})">
                   <span>🚩</span> Báo cáo
                </button>
             </div>
             <div class="q-action-btns">
                <button class="tool-btn" id="btn-translate"><span>文A</span> Dịch câu</button>
                <button class="tool-btn" id="btn-ai-explain" ${!hasAnswered ? 'disabled style="opacity:0.6;cursor:not-allowed;" title="Trả lời câu hỏi để xem giải thích"' : ''}><span>✨</span> Giải thích AI</button>
             </div>
          </div>
        `;

        // Audio Player (cho Listening)
        let mediaHtml = '';
        if (currentExamData && currentExamData.audioTitle) {
            mediaHtml = `
              <div class="audio-box">
                 <button class="audio-play-btn" id="audio-play-toggle" onclick="toggleSimulatedAudio()">▶</button>
                 <div class="audio-track">
                    <div class="audio-title">
                       <span>${currentExamData.audioTitle}</span>
                       <span id="audio-time-label">0:00 / 1:30</span>
                    </div>
                    <div class="audio-wave"><div class="audio-progress" id="audio-progress-bar"></div></div>
                 </div>
                 <button class="text-button" style="font-size:11px; padding:4px 8px; border:1px solid #bbf7d0; border-radius:4px;" onclick="$('#audio-transcript').classList.toggle('show')">Lời thoại (Transcript)</button>
              </div>
              <div class="transcript-box" id="audio-transcript">${currentExamData.audioScript || ''}</div>
            `;
        }

        // Reading Passage
        if (currentExamData && currentExamData.passageText) {
            mediaHtml = `
              <div class="passage-card">
                 <h4>📖 ${currentExamData.passageTitle || 'Reading Comprehension Passage'}</h4>
                 <p style="white-space: pre-line; margin:0;">${currentExamData.passageText}</p>
              </div>
            `;
        }

        // Body Content based on question type
        let bodyHtml = '';
        if (item.choices && item.choices.length > 0) {
            // MCQ Type
            bodyHtml = `
              <div class="question-count">Câu ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>
              <div class="options">
                ${item.choices.map((choice, index) => {
                   let cls = 'option';
                   if (hasAnswered) {
                      if (index === item.answer) cls += ' correct';
                      else if (index === uAns) cls += ' wrong';
                   }
                   return `<button class="${cls}" data-choice="${index}" ${hasAnswered ? 'disabled' : ''}>
                      <span class="letter">${String.fromCharCode(65 + index)}</span>
                      <span>${choice}</span>
                   </button>`;
                }).join('')}
              </div>
            `;
        } else if (currentExamData && currentExamData.type === 'writing') {
            // Writing Task
            bodyHtml = `
              <div class="question-count">Bài viết ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text" style="white-space:pre-line;">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>
              
              <div class="writing-box">
                 <textarea class="writing-textarea" id="writing-input" placeholder="Nhập bài viết của bạn tại đây bằng tiếng Anh..." oninput="updateWritingWordCount()">${uAns || ''}</textarea>
                 <div class="writing-stats">
                    <span>Số từ hiện tại: <strong id="word-count-num">0</strong> từ ${item.minWords ? `(Yêu cầu tối thiểu: ${item.minWords} từ)` : ''}</span>
                    <button class="primary" style="padding:8px 16px; font-size:13px;" onclick="saveWritingAnswer()">Lưu bài viết</button>
                 </div>
              </div>
            `;
        } else if (currentExamData && currentExamData.type === 'speaking') {
            // Speaking Task
            bodyHtml = `
              <div class="question-count">Phần thi nói ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text" style="white-space:pre-line;">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>

              <div class="speaking-box">
                 <p style="font-size:13px; color:#6b21a8; margin:0 0 10px;">Chuẩn bị: <strong>${item.prepTime || 30}s</strong> · Thời gian nói: <strong>${item.speakTime || 60}s</strong></p>
                 <button class="record-btn" id="record-btn" onclick="toggleSpeakingRecord()">🎙️</button>
                 <div id="record-status" style="font-size:13px; font-weight:700; color:#7e22ce;">Nhấn mic để bắt đầu ghi âm câu trả lời</div>
                 <div id="speech-playback-wrap" style="display:none; margin-top:15px;">
                    <audio id="speech-playback" controls style="width:100%; max-width:360px; margin:auto;"></audio>
                    <p style="font-size:12px; color:var(--green); font-weight:600; margin-top:6px;">✓ Đã ghi âm xong! AI sẽ đánh giá ngữ điệu và phát âm khi nộp bài.</p>
                 </div>
              </div>
            `;
        }

        let explainHtml = `
          <div class="ai-explain-box" id="ai-explain-box">
             <h4><span class="ai-icon">✨</span> Phân tích & Hướng dẫn từ AI</h4>
             <p style="white-space:pre-line; margin-bottom:8px;">${item.ai_explain || ''}</p>
             ${item.sampleAnswer ? `<div style="background:#fff; border:1px solid #bbf7d0; padding:10px; border-radius:6px; font-size:12px; color:#14532d;"><strong>Bài mẫu tham khảo:</strong><br>${item.sampleAnswer}</div>` : ''}
          </div>
        `;

        let footerHtml = `
          <div class="modal-footer" style="margin-top: 30px; border-top: 1px solid var(--line); padding-top: 20px;">
             <button class="text-button" id="prev-question" ${questionIndex === 0 ? 'style="opacity:0; pointer-events:none;"' : ''}>← Câu trước</button>
             <button class="primary" id="next-question">${questionIndex === currentQuestions.length - 1 ? (hasAnswered ? 'Xem kết quả' : 'Nộp bài') : 'Câu tiếp theo →'}</button>
          </div>
        `;

        $('#exam-main-area').innerHTML = headerHtml + mediaHtml + bodyHtml + explainHtml + footerHtml;

        // Listeners
        $$('.option:not([disabled])').forEach(button => button.addEventListener('click', () => chooseAnswer(Number(button.dataset.choice))));
        
        $('#btn-translate')?.addEventListener('click', function() {
            this.classList.toggle('active');
            $('#translated-text').classList.toggle('show');
        });
        
        $('#btn-ai-explain')?.addEventListener('click', function() {
            if (!hasAnswered) return;
            this.classList.toggle('active');
            $('#ai-explain-box').classList.toggle('show');
        });

        $('#prev-question')?.addEventListener('click', () => {
            if (questionIndex > 0) { questionIndex--; renderQuestion(); renderQuestionGrid(); }
        });
        
        $('#next-question')?.addEventListener('click', () => {
            if (questionIndex < currentQuestions.length - 1) {
                questionIndex++;
                renderQuestion();
                renderQuestionGrid();
            } else {
                finishExam();
            }
        });
        
        if (currentExamData && currentExamData.type === 'writing') {
            updateWritingWordCount();
        }
    }

    function chooseAnswer(choice) {
        if (userAnswers[questionIndex] !== null) return;
        userAnswers[questionIndex] = choice;
        if (choice === currentQuestions[questionIndex].answer) correctAnswers++;
        renderQuestion();
        renderQuestionGrid();
    }

    function updateWritingWordCount() {
        const text = $('#writing-input')?.value || '';
        const words = text.trim() ? text.trim().split(/\\s+/).length : 0;
        const numEl = $('#word-count-num');
        if (numEl) numEl.textContent = words;
    }

    function saveWritingAnswer() {
        const text = $('#writing-input')?.value || '';
        userAnswers[questionIndex] = text;
        correctAnswers++; // Simulated submission
        notify('Đã lưu bài viết của bạn.');
        renderQuestion();
        renderQuestionGrid();
    }

    function toggleSpeakingRecord() {
        isSpeakingRecording = !isSpeakingRecording;
        const btn = $('#record-btn');
        const st = $('#record-status');
        const pb = $('#speech-playback-wrap');
        
        if (isSpeakingRecording) {
            btn.classList.add('recording');
            st.textContent = 'Đang ghi âm... Nhấn lại nút để hoàn thành';
            st.style.color = '#ef4444';
            if (pb) pb.style.display = 'none';
        } else {
            btn.classList.remove('recording');
            st.textContent = 'Đã hoàn thành ghi âm bài nói!';
            st.style.color = 'var(--green)';
            if (pb) pb.style.display = 'block';
            userAnswers[questionIndex] = 'audio_recorded_sample';
            correctAnswers++;
            renderQuestionGrid();
        }
    }

    function toggleSimulatedAudio() {
        simulatedAudioPlaying = !simulatedAudioPlaying;
        const btn = $('#audio-play-toggle');
        const bar = $('#audio-progress-bar');
        const lbl = $('#audio-time-label');

        if (simulatedAudioPlaying) {
            btn.textContent = '⏸';
            audioTimer = setInterval(() => {
                audioProgressVal += 2;
                if (audioProgressVal > 100) {
                    audioProgressVal = 0;
                    simulatedAudioPlaying = false;
                    clearInterval(audioTimer);
                    btn.textContent = '▶';
                }
                if (bar) bar.style.width = audioProgressVal + '%';
                const curSec = Math.floor((audioProgressVal / 100) * 90);
                if (lbl) lbl.textContent = `0:${String(curSec).padStart(2,'0')} / 1:30`;
            }, 300);
        } else {
            btn.textContent = '▶';
            clearInterval(audioTimer);
        }
    }

    // ==========================================
    // 6. FINISH EXAM & CALIBRATED SCORING
    // ==========================================
    function finishExam() {
        clearInterval(examTimer);
        clearInterval(audioTimer);

        const courseConfig = courses.find(c => c.title === currentExamTitle) || { kind: 'TOEIC', skill: 'Reading' };
        const total = currentQuestions.length;
        const percentage = Math.round((correctAnswers / total) * 100);

        // Chấm điểm theo chuẩn
        let scoreSummary = null;
        if (courseConfig.kind === 'TOEIC') {
            scoreSummary = calculateToeicScore(correctAnswers, total, courseConfig.skill);
        } else {
            scoreSummary = calculateIeltsBand(correctAnswers, total, courseConfig.skill);
        }

        // Lưu lịch sử bài thi chi tiết
        const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
        const examRecord = {
            id: 'exam_' + Date.now(),
            title: currentExamTitle,
            kind: courseConfig.kind,
            skill: courseConfig.skill,
            date: new Date().toISOString(),
            score: percentage,
            scoreSummary: scoreSummary,
            correct: correctAnswers,
            total: total,
            timeSpent: (15 * 60) - timeLeft,
            questions: currentQuestions,
            userAnswers: [...userAnswers]
        };
        history.unshift(examRecord);
        localStorage.setItem('lingua-history', JSON.stringify(history.slice(0, 50)));

        // Hiển thị modal kết quả
        $('#exam-content').innerHTML = `
          <div class="result" style="margin-top: 20px;">
             <div class="result-score" style="width:110px; height:110px; font-size:32px;">${percentage}%</div>
             <h2>${percentage >= 70 ? 'Xuất sắc! Kết quả rất ấn tượng 🌟' : 'Đã hoàn thành bài thi! Cố gắng luyện thêm nhé 💪'}</h2>
             
             <div class="result-score-card">
                <div class="result-score-box">
                   <small>QUY ĐỔI ${courseConfig.kind}</small>
                   <strong>${courseConfig.kind === 'TOEIC' ? scoreSummary.display : scoreSummary.display}</strong>
                </div>
                <div class="result-score-box">
                   <small>SỐ CÂU ĐÚNG</small>
                   <strong>${correctAnswers} / ${total}</strong>
                </div>
                <div class="result-score-box">
                   <small>THỜI GIAN LÀM</small>
                   <strong>${Math.floor(((15*60)-timeLeft)/60)}p ${((15*60)-timeLeft)%60}s</strong>
                </div>
             </div>

             <p style="color:var(--muted); font-size:13px; max-width:550px; margin:0 auto 20px;">
                Kết quả bài thi đã được lưu vào lịch sử học tập cá nhân. Bạn có thể xem lại chi tiết từng câu làm đúng / sai để rút kinh nghiệm.
             </p>

             <div style="display:flex; justify-content:center; gap:12px;">
                <button class="primary" onclick="openReviewModalFromLatest()">Xem lại chi tiết bài làm 🔍</button>
                <button class="text-button" style="border:1px solid var(--line); border-radius:8px; padding:10px 16px;" onclick="closeExam()">Quay lại danh sách đề</button>
             </div>
          </div>
        `;

        updateScores();
        renderProfileView();
    }

    function closeExam() {
        clearInterval(examTimer);
        clearInterval(audioTimer);
        $('#exam-backdrop').classList.remove('open');
        document.body.style.overflow = '';
    }

    // ==========================================
    // 7. REVIEW MODAL (XEM LẠI BÀI THI TỪ LỊCH SỬ)
    // ==========================================
    function openReviewModalFromLatest() {
        closeExam();
        openReviewModal(0);
    }

    function openReviewModal(historyIndex) {
        const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
        const record = history[historyIndex];
        if (!record) return;

        $('#review-exam-label').textContent = `Xem lại: ${record.title}`;
        $('#review-exam-meta').textContent = `${new Date(record.date).toLocaleString('vi-VN')} · Đúng ${record.correct}/${record.total} câu · ${record.scoreSummary ? record.scoreSummary.display : record.score + '%'}`;
        
        const qList = record.questions || [];
        const uAnsList = record.userAnswers || [];

        $('#review-content').innerHTML = qList.map((q, i) => {
            const uAns = uAnsList[i];
            const isCorrect = uAns === q.answer;
            const isSkipped = uAns === null || uAns === undefined;
            const statusClass = isSkipped ? 'is-skipped' : (isCorrect ? 'is-correct' : 'is-wrong');
            const statusBadge = isSkipped ? '<span class="skill-pill" style="background:#e2e8f0; color:#475569;">Bỏ qua</span>' : 
                                (isCorrect ? '<span class="skill-pill" style="background:#dcfce7; color:#15803d;">✓ Đúng</span>' : 
                                '<span class="skill-pill" style="background:#fee2e2; color:#b91c1c;">✗ Sai</span>');

            return `
              <div class="review-item ${statusClass}">
                 <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <div style="display:flex; align-items:center; gap:8px;">
                       <strong>Câu ${i + 1}</strong>
                       ${statusBadge}
                    </div>
                    <div style="display:flex; gap:6px;">
                       <button class="q-tool-btn" onclick="toggleBookmark('${record.title}', ${i})">⭐ Lưu câu</button>
                       <button class="q-tool-btn" onclick="openReportModal('${record.title}', ${i})">🚩 Báo cáo</button>
                    </div>
                 </div>

                 <h4 style="margin:0 0 6px; font-size:14px;">${q.text}</h4>
                 ${q.translated ? `<p style="margin:0 0 10px; font-size:12px; color:var(--muted); font-style:italic;">${q.translated}</p>` : ''}

                 ${q.choices ? `
                 <div style="display:grid; gap:6px; margin-bottom:12px;">
                    ${q.choices.map((c, cIdx) => {
                       let optStyle = 'background:#fff; border:1px solid #e2e8f0; color:#334155;';
                       if (cIdx === q.answer) optStyle = 'background:#f0fdf4; border:1px solid #22c55e; color:#15803d; font-weight:700;';
                       else if (cIdx === uAns && !isCorrect) optStyle = 'background:#fef2f2; border:1px solid #ef4444; color:#b91c1c; text-decoration:line-through;';
                       return `<div style="padding:8px 12px; border-radius:6px; font-size:13px; display:flex; gap:8px; ${optStyle}">
                          <span>${String.fromCharCode(65 + cIdx)}.</span>
                          <span>${c}</span>
                          ${cIdx === q.answer ? '<span style="margin-left:auto;">✓ Đáp án chuẩn</span>' : ''}
                          ${cIdx === uAns && !isCorrect ? '<span style="margin-left:auto;">(Bạn đã chọn)</span>' : ''}
                       </div>`;
                    }).join('')}
                 </div>
                 ` : (uAns ? `<div style="background:#f8fafc; padding:8px 12px; border-radius:6px; font-size:13px; margin-bottom:10px;"><strong>Bài làm của bạn:</strong> ${uAns}</div>` : '')}

                 <div style="background:#f8fafc; border-left:3px solid var(--green); padding:10px 12px; border-radius:6px; font-size:12.5px; line-height:1.6; color:#334155;">
                    <strong style="color:var(--green-dark);">✨ Giải thích chi tiết:</strong> ${q.ai_explain || 'Không có giải thích.'}
                 </div>
              </div>
            `;
        }).join('');

        $('#review-modal').classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeReviewModal() {
        $('#review-modal').classList.remove('open');
        document.body.style.overflow = '';
    }

    // ==========================================
    // 8. UPDATE PROGRESS & HISTORY
    // ==========================================
    function updateScores() {
        const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
        
        // Seed initial history if totally empty
        if (history.length === 0) {
            history.push({
                id: 'exam_seed_1',
                title: 'TOEIC Reading · Part 5: Incomplete Sentences',
                kind: 'TOEIC',
                skill: 'Reading',
                date: new Date(Date.now() - 24*3600*1000).toISOString(),
                score: 80,
                scoreSummary: { display: '420 pts (B2)' },
                correct: 4,
                total: 5,
                timeSpent: 360,
                questions: examDatabase['TOEIC Reading · Part 5: Incomplete Sentences']?.questions || questions,
                userAnswers: [2, 1, 0, 0, 1]
            });
            localStorage.setItem('lingua-history', JSON.stringify(history));
        }

        const totalExams = history.length;
        const totalQuestions = history.reduce((sum, item) => sum + (item.total || 0), 0);
        const totalCorrect = history.reduce((sum, item) => sum + (item.correct || 0), 0);
        const average = totalQuestions > 0 ? Math.round((totalCorrect / totalQuestions) * 100) : 0;
        
        if ($('#progress-exams')) $('#progress-exams').textContent = totalExams;
        if ($('#progress-questions')) $('#progress-questions').textContent = totalQuestions;
        if ($('#progress-average')) $('#progress-average').textContent = `${average}%`;
        
        if ($('#question-total')) $('#question-total').innerHTML = `${totalQuestions} <small>câu</small>`;
        if ($('#average-score')) $('#average-score').innerHTML = `${average}<small>%</small>`;
        
        // Render rich history list
        const list = $('#history-list');
        if (list) {
            list.innerHTML = history.slice(0, 10).map((item, index) => {
                const d = new Date(item.date);
                const dateStr = `${d.getDate()}/${d.getMonth()+1}/${d.getFullYear()} ${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;
                const m = Math.floor((item.timeSpent || 0) / 60);
                const s = (item.timeSpent || 0) % 60;
                const scoreBadge = item.scoreSummary ? item.scoreSummary.display : `${item.score}%`;
                
                return `
                  <div class="history-item" style="cursor:default;">
                     <div class="history-info" style="flex:1;">
                        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
                           <span class="skill-pill ${(item.skill || 'Reading').toLowerCase()}">${item.skill || 'Test'}</span>
                           <h4 style="margin:0; font-size:13.5px;">${item.title}</h4>
                        </div>
                        <p style="margin:0; font-size:11.5px; color:var(--muted);">${dateStr} · Đúng ${item.correct}/${item.total} câu · ${m}p ${s}s</p>
                     </div>
                     <div style="display:flex; align-items:center; gap:12px;">
                        <div class="score-chip ${item.score >= 80 ? 'high' : (item.score >= 50 ? 'mid' : 'low')}">${scoreBadge}</div>
                        <button class="text-button" style="padding:6px 10px; font-size:12px; border:1px solid var(--line); border-radius:6px;" onclick="openReviewModal(${index})">Xem lại 🔍</button>
                     </div>
                  </div>
                `;
            }).join('');
        }

        // Render bar chart
        const chart = $('#score-chart');
        if (chart) {
            const recent = history.slice(0, 7).reverse();
            chart.innerHTML = recent.map((item, i) => `
              <div class="bar-wrap" style="align-items: center; justify-content: flex-end; display: flex; flex-direction: column; height: 100%; gap: 7px;">
                 <div class="bar" style="height:${Math.max(item.score, 8)}%; background: ${item.score >= 80 ? 'var(--green)' : (item.score >= 50 ? '#94bd6f' : 'var(--coral)')}; width: 100%;" title="${item.title}: ${item.score}%"></div>
                 <span style="font-size:10px;">#${i+1}</span>
              </div>
            `).join('');
        }
    }

    // ==========================================
    // 9. NAVIGATION & INITIALIZATION
    // ==========================================
    function showView(name) {
      $$('.view').forEach(view => view.classList.toggle('active', view.id === `view-${name}`));
      $$('.nav button').forEach(button => button.classList.toggle('active', button.dataset.view === name));
      
      const breadcrumbNames = {
          overview: 'Tổng quan',
          practice: 'Luyện đề 4 kỹ năng',
          vocabulary: 'Từ vựng',
          progress: 'Tiến độ & Lịch sử',
          bookmarks: 'Đã lưu & Báo cáo',
          profile: 'Hồ sơ mục tiêu'
      };
      if ($('#crumb-current')) $('#crumb-current').textContent = breadcrumbNames[name] || 'Không gian học';
      
      if (name === 'practice') renderCourses();
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();
      
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Close modals on Escape key
    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') {
            closeExam();
            closeReportModal();
            closeReviewModal();
        }
    });

    renderCourses();
    showWord(0);
    updateScores();
    renderBookmarksView();
    renderProfileView();'''

content = content[:start_idx] + new_js + content[end_idx + len(end_marker):]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Full 4-skills engine, scoring, history review, bookmarks & reports, and profile successfully injected!")
