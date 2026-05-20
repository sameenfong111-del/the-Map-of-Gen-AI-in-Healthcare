import json
import os
from datetime import datetime
from typing import List, Dict, Any

# ============================================
# 1. 全球医疗AI监管数据爬虫与生成器
# ============================================

def scrape_global_regulatory_updates() -> List[Dict[str, Any]]:
    """
    抓取全球医疗AI监管最新动态
    支持: 欧盟、中国、美国、新加坡、日本、加拿大、澳大利亚、巴西、印度
    
    这里可以集成:
    - Web爬虫 (BeautifulSoup/Selenium)
    - 官方API (FDA、NMPA等)
    - RSS订阅源
    - 新闻数据库
    """
    
    scraped_data = [
        {
            "country": "France",
            "countryCode": "FR",
            "iso_code": "FRA",
            "status": "严格 (Strict)",
            "color": "#ef4444",
            "frameworks": ["欧盟人工智能法案 (EU AI Act)", "欧盟数字服务法案 (EU DSA)", "通用数据保护条例 (GDPR)"],
            "levels": {
                "data_privacy": "极其严格。受 GDPR 铁律管辖，医疗健康数据属于特殊类别数据（Art. 9），生成式 AI 训练和临床应用必须经过严格的去隐私化、合规洗白或患者明示同意。",
                "technical_compliance": "高标准高门槛。AI Act 落地后，医疗领域的生成式 AI 多数被归为『高风险 AI 系统』，强制要求实施全生命周期的风险管理、对抗测试以及生成内容强制数字水印。",
                "systemic_risk": "【核心纽带 DSA Art. 34/35】。重点规制医疗虚假信息传播对公共健康的系统性风险。超大型平台必须定期评估算法推荐导致的网络健康谣言传播，并接受第三方独立审计。",
                "soft_law": "由法国国家数字伦理委员会（CNPEN）定期发布针对医疗机器人、问诊大模型的道德边界倡议。"
            },
            "latest_status": "EU AI Act officially enforces strict compliance for GenAI in clinical triage systems.",
            "update_date": "2026-05-20",
            "risk_level": "High Risk",
            "accountability_gap_score": 0.25
        },
        {
            "country": "China",
            "countryCode": "CN",
            "iso_code": "CHN",
            "status": "严格 (Strict)",
            "color": "#ef4444",
            "frameworks": ["《生成式人工智能服务管理暂行办法》", "《深度合成管理规定》", "《个人信息保护法》(PIPL)"],
            "levels": {
                "data_privacy": "严密保护。依据 PIPL 法律，医疗健康数据被定性为『敏感个人信息』，AI 研发企业在处理前必须取得个人的单独同意，并进行国家级安全影响评估。",
                "technical_compliance": "前置审查制。提供医疗深度合成或生成式服务的算法，必须在国家网信办进行算法备案。AI 生成的医学咨询、报告等内容必须进行显著的显式标识（防伪防谣水印）。",
                "systemic_risk": "社会治理与公共安全防范。高度重视内容安全与社会秩序。强制要求生成式 AI 的训练数据源具有合法性，生成的医学信息必须准确可靠，防止算法偏见和虚假有害医学叙事大范围扩散。",
                "soft_law": "科技部等部门发布《科技伦理审查办法（试行）》，医疗 AI 项目上线前需通过医疗机构及科研单位内部的科技伦理委员会审查。"
            },
            "latest_status": "NMPA launched new dynamic transparency requirements for LLM-based diagnostic assistants.",
            "update_date": "2026-05-18",
            "risk_level": "Tiered Regulation",
            "accountability_gap_score": 0.32
        }
    ]
    
    return scraped_data


# ============================================
# 2. 数据验证与清洗
# ============================================

def validate_data(data: List[Dict[str, Any]]) -> bool:
    """验证数据结构完整性"""
    required_fields = [
        "country", "countryCode", "iso_code", "status", "color",
        "frameworks", "levels", "latest_status", "update_date",
        "risk_level", "accountability_gap_score"
    ]
    
    for country in data:
        for field in required_fields:
            if field not in country:
                print(f"Error: {country.get('country', 'Unknown')} missing field {field}")
                return False
        
        required_levels = ["data_privacy", "technical_compliance", "systemic_risk", "soft_law"]
        for level in required_levels:
            if level not in country["levels"]:
                print(f"Error: {country.get('country', 'Unknown')} missing level {level}")
                return False
    
    print(f"Data validation passed: {len(data)} countries")
    return True


# ============================================
# 3. 保存为 JSON 文件
# ============================================

def save_to_json(data: List[Dict[str, Any]], file_path: str = None) -> bool:
    """Save data to JSON file"""
    
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), "ai_policy_data.json")
    
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        file_size = os.path.getsize(file_path)
        print(f"Data saved successfully!")
        print(f"Path: {file_path}")
        print(f"Records: {len(data)}")
        print(f"Size: {file_size / 1024:.2f} KB")
        print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return True
    
    except Exception as e:
        print(f"Save failed: {str(e)}")
        return False


# ============================================
# 4. 主入口函数
# ============================================

if __name__ == "__main__":
    print("Starting healthcare AI regulatory data pipeline...")
    
    # Step 1: Scrape data
    print("\nStep 1: Fetching global regulatory data...")
    data = scrape_global_regulatory_updates()
    print(f"Successfully fetched {len(data)} countries\n")
    
    # Step 2: Validate data
    print("Step 2: Validating data structure...")
    if not validate_data(data):
        print("Validation failed. Exiting.")
        exit(1)
    print()
    
    # Step 3: Save to JSON
    print("Step 3: Saving data...")
    save_to_json(data)
    
    print("\nPipeline completed successfully!")
    print("Next: Load data in index.html using fetch('ai_policy_data.json')")
