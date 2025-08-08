Cloudflare Solver with SeleniumBase
This Python project uses SeleniumBase with undetected-chromedriver to automatically solve Cloudflare challenges. The script will return the cf_clearance cookie, which is necessary to access a site without being blocked.

🛠️ Installation
You need Python 3.x to run this script. 
Simply install SeleniumBase using pip:

```bash
pip install seleniumbase
```
SeleniumBase includes undetected-chromedriver, so you don't need to install it separately.

🚀 Usage
Run the script from your terminal.

```bash
python cloudflare_solver.py
```

[🎬 Watch Demo](https://raw.githubusercontent.com/Elang02/cloudflare-solver/refs/heads/main/cloudflare-solver-demo.mp4)

🖥️ Example Output
When you run the script, you should see output in your terminal similar to this:

```bash
Captcha Solved
{'_ga_CGSYCY8WMN': 'GS2.1.s1754644960$o1$g0$t1754644960$j60$l0$h0', '_ga': 'GA1.1.626773975.1754644960', 'cf_clearance': 'QC3yaVjKeOC782GNDW4pf54kGeKfYreQUMXLl3E1z5c-1754644959-1.2.1.1-Geihk0NFiKFB0ADWH748mKo2D8MLEmxfJaRBJwsQcc5g3Krn0YxYFKy5mGxUUjPxSJmu_ZlkbJLKxAo3.kmFQcJnydFlPHjr02I1YS51ftKI.9PHNnhDCzvB.7Za2lTP4u0SsXCInct0eKLMGpUhRMeYaBNIxbyy3pRSuBdDnD5noX34O.zCOczng7L5QxUqZTAKHwRKVvWCXUxVzMPpI.aBt8M3BDLa9wFDPYLvgzsvMuHrktAy31Y95vGCUMNk'}
```


📝 Notes
- Change target_url to the website you want to access.
- Use this script responsibly.
