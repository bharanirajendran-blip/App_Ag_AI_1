import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def analyze_incident(incident):
    prompt = f"""You are Sentinel, a security analyst AI.
    
Analyze this incident using ReAct format:

Incident: {incident}

Thought: [What do I need to understand?]
Action: [What should I investigate?] (simulate for now)
Observation: [What would I find?]

Continue until you have a recommendation."""

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.content[0].text


test_incidents = {
    "ssh_brute_force": """
Multiple failed SSH login attempts detected:
- Source IP: 185.220.101.x (Tor exit node)
- Target: production-web-01
- Attempts: 347 in 10 minutes
- Usernames tried: root, admin, ubuntu, ec2-user
    """,
    
    "disk_full": """
Critical alert: Disk space critical
- Server: db-primary-01
- Mount: /var/lib/postgresql
- Usage: 97%
- Growth rate: 2% per hour
    """,
    
    "suspicious_process": """
Unusual process detected:
- Server: web-app-03
- Process: /tmp/.hidden/cryptominer
- CPU usage: 98%
- Network: Outbound connections to unknown IPs
    """
}

if __name__ == "__main__":
    print("=" * 60)
    print("SENTINEL v1.0 - Security Incident Analyzer")
    print("=" * 60)
    
    for name, incident in test_incidents.items():
        print(f"\n\n{'='*60}")
        print(f"TEST CASE: {name}")
        print(f"{'='*60}")
        
        try:
            analysis = analyze_incident(incident)
            print("\nSENTINEL ANALYSIS:")
            print("-" * 60)
            print(analysis)
        except Exception as e:
            print(f"Error: {e}")
        
        print(f"\n{'='*60}\n")
