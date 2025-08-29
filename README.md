# Thai Securities Data API

🇹🇭 🇬🇧 **Free Multilingual Public JSON API for Thai Stock Market Data**

Real-time Thai securities data from the Stock Exchange of Thailand (SET) and Market for Alternative Investment (mai), updated daily and served via GitHub's global CDN in both Thai and English languages.

## 🚀 Quick Start

```bash
# Get all securities - Thai version (922 companies)
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json

# Get all securities - English version (922 companies)  
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json

# Get compact data - Thai version (faster loading)
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_th.json

# Get compact data - English version (faster loading)
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_en.json
```

## 🌐 Multilingual Support

All API endpoints are available in both Thai and English versions:

- **🇹🇭 Thai files**: `*_th.json` - Full Thai language content with original Thai company names and sector classifications
- **🇬🇧 English files**: `*_en.json` - English language content with translated company names and sector classifications

Choose the appropriate language version based on your application needs:
- Use **Thai version** for applications serving Thai users or requiring original Thai company names
- Use **English version** for international applications or English-speaking users

## 📊 API Endpoints

**Base URL**: `https://raw.githubusercontent.com/lumduan/thai-securities-data/main/`

### Thai Language Endpoints (`_th.json`)

| Endpoint | Securities | Size | Description |
|----------|------------|------|-------------|
| [`thai_securities_all_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json) | 922 | ~584KB | Complete Thai dataset with all fields |
| [`thai_securities_compact_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_th.json) | 922 | ~223KB | Essential fields only (Thai) |
| [`thai_securities_market_set_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_th.json) | 697 | ~455KB | SET market securities (Thai) |
| [`thai_securities_market_mai_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai_th.json) | 225 | ~129KB | mai market securities (Thai) |
| [`thai_securities_by_sector_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_by_sector_th.json) | 922 | ~616KB | Grouped by 28 business sectors (Thai) |
| [`metadata_th.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_th.json) | - | ~3.5KB | Thai API statistics and information |

### English Language Endpoints (`_en.json`)

| Endpoint | Securities | Size | Description |
|----------|------------|------|-------------|
| [`thai_securities_all_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json) | 922 | ~340KB | Complete English dataset with all fields |
| [`thai_securities_compact_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_en.json) | 922 | ~126KB | Essential fields only (English) |
| [`thai_securities_market_set_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_en.json) | 697 | ~261KB | SET market securities (English) |
| [`thai_securities_market_mai_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai_en.json) | 225 | ~79KB | mai market securities (English) |
| [`thai_securities_by_sector_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_by_sector_en.json) | 922 | ~371KB | Grouped by 28 business sectors (English) |
| [`metadata_en.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_en.json) | - | ~2.4KB | English API statistics and information |

## 💻 Usage Examples

### JavaScript

```javascript
// Fetch all securities (Thai version)
const responseTh = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json');
const securitiesTh = await responseTh.json();
console.log(`Loaded ${securitiesTh.length} Thai securities`);

// Fetch all securities (English version)  
const responseEn = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json');
const securitiesEn = await responseEn.json();
console.log(`Loaded ${securitiesEn.length} English securities`);

// Fetch compact data for better performance (Thai)
const compactDataTh = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_th.json');
const compactSecuritiesTh = await compactDataTh.json();

// Fetch compact data for better performance (English)
const compactDataEn = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_en.json');
const compactSecuritiesEn = await compactDataEn.json();

// Get API metadata (Thai)
const metadataTh = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_th.json');
const apiInfoTh = await metadataTh.json();
console.log(`Thai API last updated: ${apiInfoTh.last_updated}`);

// Get API metadata (English)
const metadataEn = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_en.json');
const apiInfoEn = await metadataEn.json();
console.log(`English API last updated: ${apiInfoEn.last_updated}`);
```

### Python

```python
import pandas as pd
import requests

# Using pandas - Thai version (recommended for Thai data analysis)
df_th = pd.read_json('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json')
print(f"Loaded {len(df_th)} Thai securities")

# Using pandas - English version (recommended for international users)
df_en = pd.read_json('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json')
print(f"Loaded {len(df_en)} English securities")

# Using requests for Thai data
response_th = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_th.json')
securities_th = response_th.json()

# Using requests for English data
response_en = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_en.json')
securities_en = response_en.json()

# Get specific market data (Thai SET)
set_data_th = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_th.json')
set_securities_th = set_data_th.json()
print(f"SET market (Thai) has {len(set_securities_th)} securities")

# Get specific market data (English SET)
set_data_en = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_en.json')
set_securities_en = set_data_en.json()
print(f"SET market (English) has {len(set_securities_en)} securities")
```

### cURL & jq

```bash
# Download complete dataset (Thai)
curl -o thai_securities_th.json https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json

# Download complete dataset (English)
curl -o thai_securities_en.json https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json

# Count securities by market (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq 'group_by(.market) | map({market: .[0].market, count: length})'

# Count securities by market (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json | jq 'group_by(.market) | map({market: .[0].market, count: length})'

# Filter by sector (Thai - Energy & Utilities)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq '.[] | select(.sector == "พลังงานและสาธารณูปโภค")'

# Get latest update timestamp (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_th.json | jq -r '.last_updated'

# Get latest update timestamp (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata_en.json | jq -r '.last_updated'
```

### PHP

```php
// Fetch Thai securities data
$url_th = 'https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_th.json';
$data_th = json_decode(file_get_contents($url_th), true);
echo "Loaded " . count($data_th) . " Thai securities\n";

// Fetch English securities data
$url_en = 'https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact_en.json';
$data_en = json_decode(file_get_contents($url_en), true);
echo "Loaded " . count($data_en) . " English securities\n";

// Filter SET market only (Thai)
$setSecurities_th = array_filter($data_th, function($security) {
    return $security['market'] === 'SET';
});

// Filter SET market only (English)
$setSecurities_en = array_filter($data_en, function($security) {
    return $security['market'] === 'SET';
});

echo "SET market: " . count($setSecurities_th) . " Thai securities, " . count($setSecurities_en) . " English securities\n";
```

## 📋 Data Schema

### Thai Complete Dataset (`thai_securities_all_th.json`)

```json
{
  "symbol": "PTT",
  "name": "บริษัท ปิโตรเลียมแห่งประเทศไทย จำกัด (มหาชน)",
  "market": "SET",
  "industry": "พลังงาน",
  "sector": "พลังงานและสาธารณูปโภค",
  "address": "555 ถนนวิภาวดีรังสิต แขวงจตุจักร เขตจตุจักร กรุงเทพมหานคร",
  "zip": "10900",
  "tel": "0-2537-2000",
  "fax": "0-2537-3498",
  "web": "www.pttplc.com"
}
```

### English Complete Dataset (`thai_securities_all_en.json`)

```json
{
  "symbol": "PTT",
  "name": "PTT Public Company Limited",
  "market": "SET",
  "industry": "Energy",
  "sector": "Energy & Utilities",
  "address": "555 Vibhavadi Rangsit Road, Chatuchak, Bangkok",
  "zip": "10900",
  "tel": "0-2537-2000",
  "fax": "0-2537-3498",
  "web": "www.pttplc.com"
}
```

### Compact Dataset Schema (Both Languages)

```json
{
  "symbol": "PTT",
  "name": "บริษัท ปิโตรเลียมแห่งประเทศไทย จำกัด (มหาชน)", // Thai version
  "name": "PTT Public Company Limited", // English version
  "market": "SET",
  "sector": "พลังงานและสาธารณูปโภค" // Thai version
  "sector": "Energy & Utilities" // English version
}
```

## 🔄 Update Schedule

Data is automatically updated **Daily**:
- **07:00 Thailand time (GMT+7)** - Pre-market update


Check [`metadata.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json) for the exact last update timestamp.

## 📈 Performance & Reliability

- **🚀 High Capacity**: 10,000+ requests per minute
- **🌍 Global CDN**: Sub-200ms response times worldwide via GitHub's infrastructure
- **⚡ 99.9% Uptime**: Enterprise-grade reliability
- **💰 Free**: No API keys, rate limits, or costs
- **📱 CORS Enabled**: Works from web browsers

## 📊 Current Statistics

- **Total Securities**: 922 companies
- **SET Market**: 697 securities
- **mai Market**: 225 securities  
- **Business Sectors**: 28 categories
- **Languages**: Thai (🇹🇭) and English (🇬🇧)
- **Data Sources**:
  - Thai: [Listed Companies (Thai)](https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_th_TH.xls)
  - English: [Listed Companies (English)](https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_en_US.xls)

## 💡 Use Cases

- **📱 Financial Apps**: Stock screeners, portfolio trackers (multilingual support)
- **📊 Data Analysis**: Market research, sector analysis, academic studies
- **🎓 Educational**: Learning Thai stock market, fintech projects
- **🔧 API Development**: Backend services, mobile apps, trading bots
- **📈 Dashboards**: Real-time market monitoring, business intelligence
- **🌍 International Applications**: Serve both Thai and international users

## 🛠️ Integration Best Practices

1. **🌐 Choose Language**: Use Thai version for local users, English for international
2. **🎯 Use Compact Endpoint**: For better performance when you only need basic fields
3. **💾 Implement Caching**: Data updates daily, cache responses appropriately
4. **🛡️ Error Handling**: Always implement proper error handling for network requests
5. **📡 Monitor Metadata**: Check `metadata_th.json` / `metadata_en.json` for update timestamps
6. **⚡ Rate Limiting**: Respect GitHub's infrastructure, implement client-side rate limiting
7. **🔄 Polling Strategy**: Check for updates every few hours rather than continuous polling

## 🔍 Filtering & Querying Examples

### By Market

```bash
# GET SET securities only (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_th.json

# GET SET securities only (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set_en.json

# GET mai securities only (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai_th.json

# GET mai securities only (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai_en.json
```

### By Sector

```bash
# Energy & Utilities companies (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq '.[] | select(.sector == "พลังงานและสาธารณูปโภค")'

# Energy & Utilities companies (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json | jq '.[] | select(.sector == "Energy & Utilities")'

# Banking & Finance companies (Thai)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq '.[] | select(.sector == "เงินทุนและหลักทรัพย์")'

# Banking & Finance companies (English)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json | jq '.[] | select(.sector == "Banking & Finance")'
```

### Search by Name

```bash
# Find companies with "ธนาคาร" (Bank) in Thai name
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq '.[] | select(.name | contains("ธนาคาร"))'

# Find companies with "Bank" in English name
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json | jq '.[] | select(.name | contains("Bank"))'

# Find companies with "โรงพยาบาล" (Hospital) in Thai name
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_th.json | jq '.[] | select(.name | contains("โรงพยาบาล"))'

# Find companies with "Hospital" in English name
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all_en.json | jq '.[] | select(.name | contains("Hospital"))'
```

## 🤝 Contributing & Support

- **🐛 Report Issues**: [Main Repository Issues](https://github.com/lumduan/update_market_summary/issues)
- **💡 Feature Requests**: Open an issue with your suggestions
- **📧 Contact**: For technical support or business inquiries
- **⭐ Star**: If this API is useful for your project!

## 📄 License & Terms

- **Data License**: Public data from Stock Exchange of Thailand
- **API License**: MIT License for the processing pipeline
- **Usage**: Free for educational, research, and commercial use
- **Attribution**: Not required but appreciated

## 🙏 Acknowledgments

- **Data Source**: [Stock Exchange of Thailand (SET)](https://www.set.or.th/)
- **Infrastructure**: Powered by GitHub's global CDN
- **Automation**: Fully automated data pipeline with validation and monitoring

---

**📊 API Status**: ✅ **Active** • **🔄 Auto-Updates**: Daily • **📈 Securities**: 922 • **🌐 Languages**: Thai & English • **⚡ Capacity**: 10K+ req/min

**Last Repository Update**: 2025-08-29 • **Data Updates**: Daily • **Uptime**: 99.9%

---

> 💡 **Tip**: Star this repository to stay updated with improvements and new features!

> 🌍 **New**: Now available in both Thai (🇹🇭) and English (🇬🇧) versions for enhanced international accessibility!
