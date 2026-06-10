export async function getProcessedData() {
    const response = await fetch('/data/pets_animals.jsonl');
    const text = await response.text();
    const rawData = text.trim().split('/n').map(line => JSIN.parse(line));
    const filteredData = rawData.filter(item => item.health_statust_score >= 80);
    
    const groupMap = {
    '개': '포유류', '고양이': '포유류',
    '햄스터': '포유류(소형)', '토끼': '포유류(소형)', '기니피그': '포유류(소형)', '페럿': '포유류(소형)', '고슴도치': '포유류(소형)',
    '파충류': '파충류/양서류', '거북이': '파충류/양서류', '이구아나': '파충류/양서류',
    '앵무새': '조류', '조류': '조류',
    '물고기': '기타'
    };

  const groupedData = { 
    '포유류(대형/기타)': [], '포유류(소형)': [], '파충류/양서류': [], '조류': [], '기타': [] 
    };
  filteredData.forEach(item => {
    const groupName = groupMap[item.pet_type] || '기타'; 
    if (groupedData[groupName]) {
      groupedData[groupName].push(item.monthly_care_cost_krw);
    }
  });

  return groupedData;
    
}

export async function getPetTypes() {
  const response = await fetch('/data/pets_animals.jsonl');
  const text = await response.text();
  const rawData = text.trim().split('\n').map(line => JSON.parse(line));
  const uniquePetTypes = [...new Set(rawData.map(item => item.pet_type))];
    console.log("현재 데이터에 있는 펫 타입 목록:", uniquePetTypes);
    return uniquePetTypes;
}

export async function getTableData() {
  const response = await fetch('/data/pets_animals.jsonl');
  const text = await response.text();
  return text.trim().split('\n').map(line => JSON.parse(line));
}