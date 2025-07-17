# Thai Securities Data API

🇹🇭 **Free Public API for Thai Stock Market Securities Data**

This repository provides up-to-date Thai securities data from the Stock Exchange of Thailand (SET) and Market for Alternative Investment (mai) in multiple JSON formats.

## 📊 Available Data

- **Total Securities**: 900+ companies
- **Markets**: SET and mai
- **Sectors**: 25+ business sectors
- **Update Frequency**: 3 times daily (7 AM, 12 PM, 6 PM Thailand time)

## 🌐 API Endpoints

All endpoints are served via GitHub's global CDN for high performance and reliability.

### Base URL
```
https://raw.githubusercontent.com/lumduan/thai-securities-data/main/
```

### Available Files

| File | Size | Description |
|------|------|-------------|
| [`thai_securities_all.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json) | ~570KB | Complete dataset with all fields |
| [`thai_securities_compact.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json) | ~220KB | Minimal fields (symbol, name, market, sector) |
| [`thai_securities_by_sector.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_by_sector.json) | ~640KB | Organized by business sectors |
| [`thai_securities_market_set.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_set.json) | ~450KB | SET market securities only |
| [`thai_securities_market_mai.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_market_mai.json) | ~130KB | mai market securities only |
| [`metadata.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json) | ~4KB | Update information and statistics |

## 🚀 Usage Examples

### JavaScript
```javascript
// Fetch all securities
const response = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json');
const securities = await response.json();

// Fetch compact data (faster)
const compactData = await fetch('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json')
  .then(r => r.json());
```

### Python
```python
import pandas as pd
import requests

# Using pandas (recommended)
df = pd.read_json('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json')

# Using requests
response = requests.get('https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json')
data = response.json()
```

### cURL
```bash
# Download complete dataset
curl -O https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_all.json

# View metadata
curl https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json
```

### PHP
```php
// Fetch securities data
$url = 'https://raw.githubusercontent.com/lumduan/thai-securities-data/main/thai_securities_compact.json';
$data = json_decode(file_get_contents($url), true);
```

## 📈 Performance

- **Capacity**: 10,000+ requests/minute
- **Global CDN**: Sub-100ms response times worldwide
- **Availability**: 99.9% uptime via GitHub infrastructure
- **Cost**: Completely free

## 📋 Data Schema

### Complete Dataset Fields
```json
{
  "symbol": "Stock symbol (e.g., PTT, SCB)",
  "name": "Company name in Thai",
  "market": "Market (SET or mai)",
  "industry": "Industry classification",
  "sector": "Business sector",
  "address": "Company address",
  "zip": "Postal code",
  "tel": "Phone number",
  "fax": "Fax number",
  "web": "Website URL"
}
```

### Compact Dataset Fields
```json
{
  "symbol": "Stock symbol",
  "name": "Company name",
  "market": "Market (SET/mai)",
  "sector": "Business sector"
}
```

## 🔄 Update Schedule

Data is automatically updated:
- **07:00 Thailand time** - Pre-market update
- **12:00 Thailand time** - Midday refresh
- **18:00 Thailand time** - Post-market update

## 📊 Statistics

Check the [`metadata.json`](https://raw.githubusercontent.com/lumduan/thai-securities-data/main/metadata.json) file for:
- Last update timestamp
- Total number of securities
- Market breakdown
- Sector statistics

## 💡 Use Cases

- **Financial Applications**: Stock screeners, portfolio tools
- **Data Analysis**: Market research, sector analysis
- **Educational Projects**: Learning Thai stock market
- **API Development**: Backend services, mobile apps

## 🛠️ Integration Tips

1. **Cache responses** in your application to reduce API calls
2. **Use compact endpoint** for faster loading when you only need basic info
3. **Monitor metadata.json** to check for updates
4. **Implement error handling** for network requests

## 🤝 Contributing

This data is automatically generated from official SET sources. For issues or suggestions:
- Open an issue in the [main repository](https://github.com/lumduan/update_market_summary)
- Contact: [your-email@example.com]

## 📄 License

This data is provided for educational and non-commercial use. Please respect the terms of use from the original data source (SET).

## 🙏 Acknowledgments

- Data source: [Stock Exchange of Thailand (SET)](https://www.set.or.th/)
- Powered by GitHub's global CDN infrastructure

---

**Last Updated**: Automatically updated 3 times daily  
**Data Source**: Stock Exchange of Thailand (SET)  
**API Status**: ✅ Active
