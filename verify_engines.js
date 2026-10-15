const fs = require('fs');

// Mock browser window
global.window = global;

// Load toeic_engine.js
require('./toeic/toeic_engine.js');
// Load ielts_engine.js
require('./ielts/ielts_engine.js');

const courses = [
  ...(window.toeicCourses || []),
  ...(window.ieltsCourses || [])
];

const examDatabase = Object.assign({}, window.toeicExams || {}, window.ieltsExams || {});

console.log('--- TEST VERIFICATION ---');
console.log(`Total courses: ${courses.length}`);
const actualTests = courses.filter(c => c.isActualTest);
console.log(`Total Actual Tests (isActualTest=true): ${actualTests.length}`);

const etsTests = courses.filter(c => c.source === 'ETS');
console.log(`Total ETS Tests: ${etsTests.length}`);

const cambridgeTests = courses.filter(c => c.source === 'Cambridge');
console.log(`Total Cambridge Tests: ${cambridgeTests.length}`);

console.log(`Total examDatabase entries: ${Object.keys(examDatabase).length}`);

// Check if each course has an entry in examDatabase (or fallback)
let missingDb = 0;
courses.forEach(c => {
  if (!examDatabase[c.title]) {
    missingDb++;
    console.log(`  * Missing in examDatabase: ${c.title}`);
  }
});

console.log(`Courses missing in examDatabase: ${missingDb}`);
console.log('ALL VERIFICATIONS FINISHED.');
