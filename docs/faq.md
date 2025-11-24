Frequently Asked Questions (FAQ)
Below are the most common questions new users have about Franklin. This list will grow as the community expands.
1. What exactly is Franklin?
Franklin is a local-first AI engine that runs on your machine using Docker. It can read files, summarize content, run tools, and use local or cloud AI models — all without sending your private data anywhere unless you choose to.
2. Does Franklin upload my files to the cloud?
No. Everything stays on your hardware. The only time anything leaves your machine is when you choose to use the GPT fallback — and even then, only the text you type is sent.
3. Do I need a powerful PC to run Franklin?
No. Franklin is lightweight and runs on almost anything that can run Docker, including laptops, homelab servers, old PCs, Proxmox containers, and Debian/Ubuntu machines. Local AI models may require more RAM, but Franklin itself is efficient.
4. Do I need the internet to use Franklin?
Only for GPT fallback (optional), updates, and support/documentation. All local tools and TinyLlama work fully offline.
5. How do I update Franklin?
Updates are done through Docker: pull the latest version, rebuild the containers, and restart Franklin. We’ll never force an update, and your settings remain intact.
6. Where do I enter my license key?
Inside the Web UI: Settings → License. If you reinstall Franklin, your key will still work.
7. What if I lose my license key?
Email support and we will re-send it:
support@dfrankstudioz.com
. No fees, no hassle.
8. My local model isn’t working — what should I check?
Start with these checks: the Ollama container is running, the model exists in ~/.ollama or the mounted volume, ports aren’t blocked, and restart the container after installing a new model. These steps fix most local-model issues.
9. The Web UI isn’t loading — what now?
Check whether the Franklin container is running, inspect container logs for errors, verify you’re using the right URL (port 9006), and rebuild after recent updates. UI issues are usually a simple configuration fix.
10. Can I use Franklin on multiple devices?
Yes — as long as those devices can access your server on the network. Run Franklin on one machine and connect from phone, laptop, tablet, or another PC. It’s local-network friendly.
11. Will Franklin ever have plugins, dashboards, or more tools?
Yes — Franklin is being actively expanded. Plugins, system dashboards, and automation tools are part of the roadmap, and remain local-first.
12. Where do I get help if this FAQ doesn’t solve my problem?
You can reach us anytime: documentation (basic guides and setup steps), Discord for community help, or email:
support@dfrankstudioz.com
. We keep support personal and simple.
If you want these FAQs exported to Markdown for the docs, or need a shorter "quick-start" FAQ card for the homepage, I can generate those next.