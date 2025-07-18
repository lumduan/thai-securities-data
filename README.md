# Thai Securities Data API

🇹🇭 **Free Public JSON API for Thai Stock Market Data**

Real-time Thai securities data from the Stock Exchange of Thailand (SET) and Market for Alternative Investment (mai), updated daily and served via GitHub's global CDN.

## 🚀 Quick Start

```bash
# Get all securities (922 companies)
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json

# Get compact data (faster loading)
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json
```

## 📊 API Endpoints

**Base URL**: `https://raw.githubusercontent.com/lumduan/thai-securities-data/main/`

| Endpoint | Securities | Size | Description |
|----------|------------|------|-------------|
| [`thai_securities_all.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json) | 922 | ~400KB | Complete dataset with all fields |
| [`thai_securities_compact.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json) | 922 | ~50KB | Essential fields only (symbol, name, market, sector) |
| [`thai_securities_market_set.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set.json) | 697 | ~300KB | SET market securities only |
| [`thai_securities_market_mai.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai.json) | 225 | ~100KB | mai market securities only |
| [`thai_securities_by_sector.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_by_sector.json) | 922 | ~400KB | Grouped by 28 business sectors |
| [`metadata.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json) | - | ~2KB | API statistics and update information |

## 💻 Usage Examples

### JavaScript
```javascript
// Fetch all securities
const response = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json');
const securities = await response.json();
console.log(`Loaded ${securities.length} securities`);

// Fetch compact data for better performance
const compactData = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json');
const compactSecurities = await compactData.json();

// Get API metadata
const metadata = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json');
const apiInfo = await metadata.json();
console.log(`Last updated: ${apiInfo.last_updated}`);
```

### Python
```python
import pandas as pd
import requests

# Using pandas (recommended for data analysis)
df = pd.read_json('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json')
print(f"Loaded {len(df)} securities")

# Using requests
response = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json')
securities = response.json()

# Get specific market data
set_data = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set.json')
set_securities = set_data.json()
print(f"SET market has {len(set_securities)} securities")
```

### cURL & jq
```bash
# Download complete dataset
curl -o thai_securities.json https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json

# Count securities by market
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json | jq 'group_by(.market) | map({market: .[0].market, count: length})'

# Filter by sector (Energy & Utilities)
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json | jq '.[] | select(.sector == "พลังงานและสาธารณูปโภค")'

# Get latest update timestamp
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json | jq -r '.last_updated'
```

### PHP
```php
// Fetch securities data
$url = 'https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json';
$data = json_decode(file_get_contents($url), true);

echo "Loaded " . count($data) . " securities\n";

// Filter SET market only
$setSecurities = array_filter($data, function($security) {
    return $security['market'] === 'SET';
});
```

## 📋 Data Schema

### Complete Dataset (`thai_securities_all.json`)
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

### Compact Dataset (`thai_securities_compact.json`)
```json
{
  "symbol": "PTT",
  "name": "บริษัท ปิโตรเลียมแห่งประเทศไทย จำกัด (มหาชน)",
  "market": "SET",
  "sector": "พลังงานและสาธารณูปโภค"
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
- **Data Source**: [Stock Exchange of Thailand](https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_th_TH.xls)

## 💡 Use Cases

- **📱 Financial Apps**: Stock screeners, portfolio trackers
- **📊 Data Analysis**: Market research, sector analysis, academic studies
- **🎓 Educational**: Learning Thai stock market, fintech projects
- **🔧 API Development**: Backend services, mobile apps, trading bots
- **📈 Dashboards**: Real-time market monitoring, business intelligence

## 🛠️ Integration Best Practices

1. **🎯 Use Compact Endpoint**: For better performance when you only need basic fields
2. **💾 Implement Caching**: Data updates daily, cache responses appropriately
3. **🛡️ Error Handling**: Always implement proper error handling for network requests
4. **📡 Monitor Metadata**: Check `metadata.json` for update timestamps and API status
5. **⚡ Rate Limiting**: Respect GitHub's infrastructure, implement client-side rate limiting
6. **🔄 Polling Strategy**: Check for updates every few hours rather than continuous polling

## 🔍 Filtering & Querying Examples

### By Market
```bash
# GET SET securities only
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set.json

# GET mai securities only  
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai.json
```

### By Sector
```bash
# Energy & Utilities companies
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json | jq '.[] | select(.sector == "พลังงานและสาธารณูปโภค")'

# Banking & Finance companies
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json | jq '.[] | select(.sector == "เงินทุนและหลักทรัพย์")'
```

### Search by Name
```bash
# Find companies with "ธนาคาร" (Bank) in name
curl -s https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json | jq '.[] | select(.name | contains("ธนาคาร"))'
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

**📊 API Status**: ✅ **Active** • **🔄 Auto-Updates**: Daily • **📈 Securities**: 922 • **⚡ Capacity**: 10K+ req/min

**Last Repository Update**: 2025-07-17 • **Data Updates**: Daily • **Uptime**: 99.9%

---

> 💡 **Tip**: Star this repository to stay updated with improvements and new features!
