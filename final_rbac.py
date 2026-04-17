import tkinter as tk
from tkinter import messagebox, ttk
import json, os, random
from datetime import datetime as dt

class Bank:
    def __init__(self, r):
        self.r, self.u, self.m, self.nb = r, None, None, []
        r.title("SmartBank"); r.geometry("950x600"); r.configure(bg="white")
        self.P, self.K, self.G, self.D, self.R, self.B = "#6A11CB", "#FF1493", "#00B894", "#2D3436", "#E74C3C", "#F8F9FA"
        self.f = "sbank.json"
        try:
            with open(self.f) as f: self.db = json.load(f)
            if "admin@bank.com" not in self.db or "pwd" not in self.db["admin@bank.com"]: raise Exception()
        except:
            self.db = {"admin@bank.com": {"name": "Admin", "pwd": "admin123", "accounts": [{"type": "Savings", "no": "1234567890", "bal": 50000.0, "history": [{"date": "16-Apr-2025", "desc": "Opening Deposit", "amt": 50000.0, "type": "CR"}]}, {"type": "Current", "no": "9876543210", "bal": 120000.0, "history": [{"date": "16-Apr-2025", "desc": "Opening Deposit", "amt": 120000.0, "type": "CR"}]}]}, "priyanka@bank.com": {"name": "Priyanka", "pwd": "123456", "accounts": [{"type": "Savings", "no": "5555566666", "bal": 25000.0, "history": [{"date": "16-Apr-2025", "desc": "Opening Deposit", "amt": 25000.0, "type": "CR"}]}]}}
            self.sv()
        self.login()
    def sv(self):
        with open(self.f, "w") as f: json.dump(self.db, f, indent=2)
    def cl(self):
        for w in self.r.winfo_children(): w.destroy()
    def cm(self):
        if self.m:
            for w in self.m.winfo_children(): w.destroy()
    def inp(self, p, l, s=None):
        tk.Label(p, text=l, font=("Arial", 11, "bold"), bg="white").pack(anchor="w", pady=(8, 2))
        e = tk.Entry(p, font=("Arial", 12), width=30, bg="#F0F0F0", relief="flat", show=s or "", highlightthickness=2, highlightcolor=self.P, highlightbackground="#DDD")
        e.pack(ipady=9, pady=3); return e
    def fa(self, no):
        for em, u in self.db.items():
            for a in u["accounts"]:
                if a["no"] == no: return em, a
        return None, None
    def login(self):
        self.cl(); self.r.geometry("950x560"); self.r.configure(bg="white")
        l = tk.Frame(self.r, bg=self.K, width=350); l.place(x=0, y=0, width=350, relheight=1)
        tk.Label(l, text="🏦", font=("Arial", 65), bg=self.K, fg="white").pack(pady=(80, 10))
        tk.Label(l, text="SmartBank", font=("Arial", 28, "bold"), bg=self.K, fg="white").pack()
        tk.Label(l, text="Secure Banking System", font=("Arial", 11), bg=self.K, fg="white").pack(pady=8)
        for t in ["🔒 Secure Login", "💳 Multiple Accounts", "🔄 Easy Transfer", "📊 Track History"]: tk.Label(l, text=t, font=("Arial", 10), bg=self.K, fg="white").pack(pady=3)
        f = tk.Frame(self.r, bg="white"); f.place(relx=0.68, rely=0.5, anchor="center")
        tk.Label(f, text="👤 Welcome Back", font=("Arial", 22, "bold"), bg="white", fg=self.P).pack(pady=(0, 20))
        e1, e2 = self.inp(f, "📧 Email"), self.inp(f, "🔒 Password", "*")
        tk.Button(f, text="LOGIN →", bg=self.P, fg="white", font=("Arial", 12, "bold"), width=28, relief="flat", cursor="hand2", command=lambda: self.dolog(e1.get().strip().lower(), e2.get())).pack(ipady=11, pady=20)
        tk.Button(f, text="Create Account →", bg="white", fg=self.K, font=("Arial", 10, "underline"), relief="flat", cursor="hand2", command=self.signup).pack()
        h = tk.Frame(f, bg="#F0EBFF", padx=12, pady=6); h.pack(fill="x", pady=10)
        tk.Label(h, text="Demo: admin@bank.com / admin123", font=("Arial", 8, "bold"), bg="#F0EBFF", fg=self.P).pack()
    def signup(self):
        self.cl(); self.r.geometry("950x600"); self.r.configure(bg="white")
        l = tk.Frame(self.r, bg=self.P, width=350); l.place(x=0, y=0, width=350, relheight=1)
        tk.Label(l, text="🏦", font=("Arial", 65), bg=self.P, fg="white").pack(pady=(80, 10))
        tk.Label(l, text="Join SmartBank", font=("Arial", 26, "bold"), bg=self.P, fg="white").pack()
        for t in ["🎁 Welcome Bonus", "💰 Free Account", "📱 Easy Banking"]: tk.Label(l, text=t, font=("Arial", 10), bg=self.P, fg="white").pack(pady=4)
        f = tk.Frame(self.r, bg="white"); f.place(relx=0.68, rely=0.5, anchor="center")
        tk.Label(f, text="📝 Create Account", font=("Arial", 22, "bold"), bg="white", fg=self.P).pack(pady=(0, 15))
        e1, e2, e3 = self.inp(f, "👤 Full Name"), self.inp(f, "📧 Email"), self.inp(f, "🔒 Password", "*")
        tk.Button(f, text="REGISTER 🚀", bg=self.K, fg="white", font=("Arial", 12, "bold"), width=28, relief="flat", cursor="hand2", command=lambda: self.doreg(e1.get().strip(), e2.get().strip().lower(), e3.get())).pack(ipady=11, pady=20)
        tk.Button(f, text="← Back to Login", bg="white", fg=self.P, font=("Arial", 10, "underline"), relief="flat", command=self.login).pack()
    def dolog(self, e, p):
        if e in self.db and self.db[e]["pwd"] == p: self.u = e; self.dash()
        else: messagebox.showerror("Error", "Invalid email or password!")
    def doreg(self, n, e, p):
        if not all([n, e, p]): return messagebox.showerror("Error", "All fields required!")
        if e in self.db: return messagebox.showerror("Error", "Email already registered!")
        self.db[e] = {"name": n, "pwd": p, "accounts": []}; self.sv(); messagebox.showinfo("✅", f"Welcome {n}! Please login."); self.login()
    def dash(self):
        self.cl(); self.r.geometry("1100x700"); self.r.configure(bg=self.B); u = self.db[self.u]
        s = tk.Frame(self.r, bg=self.D, width=210); s.pack(side="left", fill="y"); s.pack_propagate(False)
        lf = tk.Frame(s, bg=self.P, pady=15); lf.pack(fill="x"); tk.Label(lf, text="🏦 SmartBank", font=("Arial", 14, "bold"), bg=self.P, fg="white").pack()
        uf = tk.Frame(s, bg="#3D3D3D", pady=10); uf.pack(fill="x", pady=5); tk.Label(uf, text=f"👤 {u['name']}", font=("Arial", 10, "bold"), bg="#3D3D3D", fg="white").pack(); tk.Label(uf, text=self.u, font=("Arial", 8), bg="#3D3D3D", fg=self.K).pack()
        self.nb = []
        for ic, lb, cd in [("🏠","Dashboard",self.home),("➕","Open Account",self.opn),("💰","Deposit",self.dep),("💸","Withdraw",self.wdr),("🔄","Transfer",self.trf),("📊","All Details",self.det)]:
            bf = tk.Frame(s, bg=self.D, cursor="hand2"); bf.pack(fill="x")
            il = tk.Label(bf, text=ic, font=("Arial", 13), bg=self.D, fg="white", width=3); il.pack(side="left", padx=(8,4), pady=9)
            tl = tk.Label(bf, text=lb, font=("Arial", 10), bg=self.D, fg="white", anchor="w"); tl.pack(side="left", fill="x", expand=True, pady=9)
            def mk(f, i, t, c):
                def h(e=None):
                    for b, il2, tl2 in self.nb: b.configure(bg=self.D); il2.configure(bg=self.D); tl2.configure(bg=self.D)
                    f.configure(bg=self.P); i.configure(bg=self.P); t.configure(bg=self.P); c()
                return h
            cl = mk(bf, il, tl, cd); bf.bind("<Button-1>", cl); il.bind("<Button-1>", cl); tl.bind("<Button-1>", cl); self.nb.append((bf, il, tl))
        tk.Button(s, text="🚪 Logout", font=("Arial", 10, "bold"), bg=self.R, fg="white", relief="flat", pady=6, cursor="hand2", command=self.login).pack(side="bottom", fill="x", padx=8, pady=10)
        self.m = tk.Frame(self.r, bg=self.B); self.m.pack(side="right", fill="both", expand=True); self.home()
    def home(self):
        self.cm(); u = self.db[self.u]; tb = sum(a["bal"] for a in u["accounts"]); tt = sum(len(a["history"]) for a in u["accounts"])
        tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False)
        tk.Label(tp, text=f"Welcome, {u['name']}! 🎉", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        tk.Label(tp, text=dt.now().strftime("%d-%b-%Y %H:%M"), font=("Arial", 9), bg="white", fg="gray").pack(side="right", padx=20)
        cv = tk.Canvas(self.m, bg=self.B, highlightthickness=0); sb = ttk.Scrollbar(self.m, command=cv.yview); cv.configure(yscrollcommand=sb.set); sb.pack(side="right", fill="y"); cv.pack(fill="both", expand=True)
        inn = tk.Frame(cv, bg=self.B); cv.create_window((0, 0), window=inn, anchor="nw"); inn.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        sf = tk.Frame(inn, bg=self.B); sf.pack(fill="x", padx=20, pady=15)
        for i, (ic, lb, vl, cl, bg) in enumerate([("💰","Total Balance",f"₹{tb:,.0f}",self.P,"#EDE9FE"),("💳","Accounts",str(len(u["accounts"])),self.K,"#FCE7F3"),("📊","Transactions",str(tt),self.G,"#D1FAE5"),("✅","Status","Active","#E17055","#FFECD2")]):
            c = tk.Frame(sf, bg=bg, padx=18, pady=15); c.grid(row=0, column=i, padx=7, sticky="nsew"); sf.grid_columnconfigure(i, weight=1)
            tk.Label(c, text=ic, font=("Arial", 22), bg=bg).pack(anchor="w"); tk.Label(c, text=vl, font=("Arial", 16, "bold"), bg=bg, fg=cl).pack(anchor="w"); tk.Label(c, text=lb, font=("Arial", 9), bg=bg, fg="gray").pack(anchor="w")
        tk.Label(inn, text="💳 Your Bank Accounts", font=("Arial", 14, "bold"), bg=self.B, fg=self.D).pack(anchor="w", padx=20, pady=(10, 5))
        if not u["accounts"]:
            ef = tk.Frame(inn, bg="white", padx=25, pady=30); ef.pack(fill="x", padx=20); tk.Label(ef, text="🏦 No accounts yet! Click ➕ Open Account", font=("Arial", 12), bg="white", fg="gray").pack()
        for a in u["accounts"]:
            cd = tk.Frame(inn, bg="white", padx=18, pady=14, highlightbackground=self.P, highlightthickness=2); cd.pack(fill="x", padx=20, pady=6)
            lf = tk.Frame(cd, bg="white"); lf.pack(side="left"); ic = "💰" if a["type"]=="Savings" else "💼" if a["type"]=="Current" else "🔒" if a["type"]=="Fixed Deposit" else "📅"
            tk.Label(lf, text=f"{ic} {a['type']} Account", font=("Arial", 12, "bold"), bg="white", fg=self.P).pack(anchor="w"); tk.Label(lf, text=f"A/C: {a['no']} | Txns: {len(a['history'])}", font=("Arial", 9), bg="white", fg="gray").pack(anchor="w")
            tk.Label(cd, text=f"₹{a['bal']:,.2f}", font=("Arial", 18, "bold"), bg="white", fg=self.K).pack(side="right", padx=8)
        tk.Label(inn, text="⚡ Quick Actions", font=("Arial", 14, "bold"), bg=self.B, fg=self.D).pack(anchor="w", padx=20, pady=(15, 8))
        af = tk.Frame(inn, bg=self.B); af.pack(fill="x", padx=20, pady=(0, 15))
        for i, (tx, cl, cd) in enumerate([("➕ New A/C",self.P,self.opn),("💰 Deposit",self.G,self.dep),("💸 Withdraw",self.R,self.wdr),("🔄 Transfer",self.K,self.trf)]):
            tk.Button(af, text=tx, bg=cl, fg="white", font=("Arial", 10, "bold"), relief="flat", padx=18, pady=10, cursor="hand2", command=cd).grid(row=0, column=i, padx=6)
    def opn(self):
        self.cm(); tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False); tk.Label(tp, text="➕ Open New Account", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        f = tk.Frame(self.m, bg="white", padx=35, pady=25); f.pack(padx=20, pady=15, anchor="w")
        tk.Label(f, text="Account Type:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(8, 4))
        tc = ttk.Combobox(f, values=["Savings Account (Min ₹1000)","Current Account (Min ₹5000)","Fixed Deposit (Min ₹10000)","Recurring Deposit (Min ₹500)"], state="readonly", width=36, font=("Arial", 11)); tc.pack(pady=4); tc.current(0)
        tk.Label(f, text="Initial Deposit (₹):", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(15, 4))
        ae = tk.Entry(f, font=("Arial", 12), width=36, bg="#F0F0F0", relief="flat", highlightthickness=2, highlightcolor=self.P, highlightbackground="#DDD"); ae.pack(ipady=9)
        tk.Label(f, text="ℹ️ Savings ₹1K | Current ₹5K | FD ₹10K | RD ₹500", font=("Arial", 9), bg="#F0EBFF", fg=self.P).pack(fill="x", ipady=5, pady=10)
        def cr():
            try:
                am = float(ae.get()); mp = {"Savings Account":("Savings",1000),"Current Account":("Current",5000),"Fixed Deposit":("Fixed Deposit",10000),"Recurring Deposit":("Recurring Deposit",500)}
                sl = tc.get().split("(")[0].strip(); nm, mn = mp[sl]
                if am < mn: return messagebox.showerror("Error", f"Minimum ₹{mn:,} required!")
                no = str(random.randint(10**9, 10**10-1)); self.db[self.u]["accounts"].append({"type":nm,"no":no,"bal":am,"history":[{"date":dt.now().strftime("%d-%b-%Y %H:%M"),"desc":"Opening Deposit","amt":am,"type":"CR"}]}); self.sv()
                messagebox.showinfo("✅", f"{nm} Account Created!\nA/C No: {no}\nBalance: ₹{am:,.0f}"); self.home()
            except: messagebox.showerror("Error", "Enter valid amount!")
        tk.Button(f, text="Create Account ✅", bg=self.P, fg="white", font=("Arial", 12, "bold"), width=33, relief="flat", cursor="hand2", command=cr).pack(ipady=11, pady=15)
    def dep(self):
        self.cm(); u = self.db[self.u]; al = [f"{a['type']} - {a['no']} (₹{a['bal']:,.0f})" for a in u["accounts"]]
        tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False); tk.Label(tp, text="💰 Deposit Money", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        f = tk.Frame(self.m, bg="white", padx=35, pady=25); f.pack(padx=20, pady=15, anchor="w")
        if not al: tk.Label(f, text="❌ No accounts! Create one first.", font=("Arial", 12), bg="white", fg="red").pack(pady=25); return
        tk.Label(f, text="Select Account:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(8, 4))
        ac = ttk.Combobox(f, values=al, state="readonly", width=42, font=("Arial", 11)); ac.pack(pady=4); ac.current(0)
        tk.Label(f, text="Amount (₹):", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(15, 4))
        ae = tk.Entry(f, font=("Arial", 12), width=36, bg="#F0F0F0", relief="flat", highlightthickness=2, highlightcolor=self.G, highlightbackground="#DDD"); ae.pack(ipady=9)
        def dp():
            try:
                am = float(ae.get())
                if am <= 0: return messagebox.showerror("Error", "Amount must be > 0!")
                ix = ac.current(); self.db[self.u]["accounts"][ix]["bal"] += am; self.db[self.u]["accounts"][ix]["history"].append({"date":dt.now().strftime("%d-%b-%Y %H:%M"),"desc":"Cash Deposit","amt":am,"type":"CR"}); self.sv()
                messagebox.showinfo("✅", f"₹{am:,.0f} deposited!\nNew Balance: ₹{self.db[self.u]['accounts'][ix]['bal']:,.0f}"); self.home()
            except: messagebox.showerror("Error", "Enter valid amount!")
        tk.Button(f, text="Deposit 💰", bg=self.G, fg="white", font=("Arial", 12, "bold"), width=33, relief="flat", cursor="hand2", command=dp).pack(ipady=11, pady=15)
    def wdr(self):
        self.cm(); u = self.db[self.u]; al = [f"{a['type']} - {a['no']} (₹{a['bal']:,.0f})" for a in u["accounts"]]
        tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False); tk.Label(tp, text="💸 Withdraw Money", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        f = tk.Frame(self.m, bg="white", padx=35, pady=25); f.pack(padx=20, pady=15, anchor="w")
        if not al: tk.Label(f, text="❌ No accounts!", font=("Arial", 12), bg="white", fg="red").pack(pady=25); return
        tk.Label(f, text="Select Account:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(8, 4))
        ac = ttk.Combobox(f, values=al, state="readonly", width=42, font=("Arial", 11)); ac.pack(pady=4); ac.current(0)
        tk.Label(f, text="Amount (₹):", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(15, 4))
        ae = tk.Entry(f, font=("Arial", 12), width=36, bg="#F0F0F0", relief="flat", highlightthickness=2, highlightcolor=self.R, highlightbackground="#DDD"); ae.pack(ipady=9)
        def wd():
            try:
                am = float(ae.get()); ix = ac.current(); bl = self.db[self.u]["accounts"][ix]["bal"]
                if am <= 0 or am > bl: return messagebox.showerror("Error", f"Invalid! Available: ₹{bl:,.0f}")
                self.db[self.u]["accounts"][ix]["bal"] -= am; self.db[self.u]["accounts"][ix]["history"].append({"date":dt.now().strftime("%d-%b-%Y %H:%M"),"desc":"Cash Withdrawal","amt":am,"type":"DR"}); self.sv()
                messagebox.showinfo("✅", f"₹{am:,.0f} withdrawn!\nBalance: ₹{self.db[self.u]['accounts'][ix]['bal']:,.0f}"); self.home()
            except: messagebox.showerror("Error", "Enter valid amount!")
        tk.Button(f, text="Withdraw 💸", bg=self.R, fg="white", font=("Arial", 12, "bold"), width=33, relief="flat", cursor="hand2", command=wd).pack(ipady=11, pady=15)
    def trf(self):
        self.cm(); u = self.db[self.u]; al = [f"{a['type']} - {a['no']} (₹{a['bal']:,.0f})" for a in u["accounts"]]
        tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False); tk.Label(tp, text="🔄 Transfer Money", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        f = tk.Frame(self.m, bg="white", padx=35, pady=20); f.pack(padx=20, pady=10, anchor="w")
        if not al: tk.Label(f, text="❌ No accounts!", font=("Arial", 12), bg="white", fg="red").pack(pady=25); return
        tk.Label(f, text="From Account:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(8, 4))
        fc = ttk.Combobox(f, values=al, state="readonly", width=42, font=("Arial", 11)); fc.pack(pady=4); fc.current(0)
        tk.Label(f, text="To Account Number:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(12, 4))
        te = tk.Entry(f, font=("Arial", 12), width=36, bg="#F0F0F0", relief="flat", highlightthickness=2, highlightcolor=self.P, highlightbackground="#DDD"); te.pack(ipady=9)
        tk.Label(f, text="Amount (₹):", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(12, 4))
        ae = tk.Entry(f, font=("Arial", 12), width=36, bg="#F0F0F0", relief="flat", highlightthickness=2, highlightcolor=self.K, highlightbackground="#DDD"); ae.pack(ipady=9)
        tk.Label(f, text="💡 Test: 5555566666 (Priyanka)", font=("Arial", 8), bg="#FFF3E0", fg="#E17055").pack(fill="x", ipady=4, pady=6)
        def tf():
            try:
                am = float(ae.get()); ix = fc.current(); bl = self.db[self.u]["accounts"][ix]["bal"]; tn = te.get().strip(); fn = self.db[self.u]["accounts"][ix]["no"]
                if am <= 0 or am > bl: return messagebox.showerror("Error", f"Invalid! Available: ₹{bl:,.0f}")
                if fn == tn: return messagebox.showerror("Error", "Cannot transfer to same account!")
                re, ra = self.fa(tn)
                if not ra: return messagebox.showerror("Error", f"Account {tn} not found!")
                d = dt.now().strftime("%d-%b-%Y %H:%M"); self.db[self.u]["accounts"][ix]["bal"] -= am; self.db[self.u]["accounts"][ix]["history"].append({"date":d,"desc":f"Transfer to {tn}","amt":am,"type":"DR"})
                ra["bal"] += am; ra["history"].append({"date":d,"desc":f"Transfer from {fn}","amt":am,"type":"CR"}); self.sv()
                messagebox.showinfo("✅", f"₹{am:,.0f} sent to {self.db[re]['name']}!\nTo: {tn}\nBalance: ₹{self.db[self.u]['accounts'][ix]['bal']:,.0f}"); self.home()
            except: messagebox.showerror("Error", "Enter valid amount!")
        tk.Button(f, text="Transfer 🔄", bg=self.K, fg="white", font=("Arial", 12, "bold"), width=33, relief="flat", cursor="hand2", command=tf).pack(ipady=11, pady=12)
    def det(self):
        self.cm(); u = self.db[self.u]
        tp = tk.Frame(self.m, bg="white", height=55); tp.pack(fill="x"); tp.pack_propagate(False); tk.Label(tp, text="📊 Account Details & History", font=("Arial", 15, "bold"), bg="white", fg=self.P).pack(side="left", padx=20, pady=12)
        cv = tk.Canvas(self.m, bg=self.B, highlightthickness=0); sb = ttk.Scrollbar(self.m, command=cv.yview); cv.configure(yscrollcommand=sb.set); sb.pack(side="right", fill="y"); cv.pack(fill="both", expand=True)
        inn = tk.Frame(cv, bg=self.B); cv.create_window((0, 0), window=inn, anchor="nw"); inn.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        if not u["accounts"]: tk.Label(inn, text="No accounts!", font=("Arial", 13), bg=self.B, fg="gray").pack(pady=40); return
        for a in u["accounts"]:
            cf = tk.Frame(inn, bg="white", padx=18, pady=12, highlightbackground=self.P, highlightthickness=2); cf.pack(fill="x", padx=20, pady=8)
            hd = tk.Frame(cf, bg="white"); hd.pack(fill="x"); ic = "💰" if a["type"]=="Savings" else "💼" if a["type"]=="Current" else "🔒" if a["type"]=="Fixed Deposit" else "📅"
            tk.Label(hd, text=f"{ic} {a['type']} Account", font=("Arial", 13, "bold"), bg="white", fg=self.P).pack(side="left"); tk.Label(hd, text=f"₹{a['bal']:,.2f}", font=("Arial", 16, "bold"), bg="white", fg=self.K).pack(side="right")
            tk.Label(cf, text=f"Account: {a['no']}", font=("Arial", 9), bg="white", fg="gray").pack(anchor="w", pady=4); tk.Frame(cf, bg="#EEE", height=1).pack(fill="x", pady=5)
            tk.Label(cf, text="📜 Transactions:", font=("Arial", 10, "bold"), bg="white", fg=self.D).pack(anchor="w", pady=4)
            tr = ttk.Treeview(cf, columns=("Date","Desc","Amt","Type"), show="headings", height=min(len(a["history"]), 6))
            for c, w in [("Date",150),("Desc",200),("Amt",110),("Type",70)]: tr.heading(c, text=c); tr.column(c, width=w, anchor="center")
            for h in reversed(a["history"]): tr.insert("", "end", values=(h["date"], h["desc"], f"{'+'if h['type']=='CR'else'-'}₹{h['amt']:,.0f}", h["type"]))
            tr.pack(fill="x", pady=4)
if __name__ == "__main__":
    r = tk.Tk(); r.resizable(True, True); s = ttk.Style(); s.theme_use("clam"); s.configure("Treeview.Heading", background="#6A11CB", foreground="white", font=("Arial", 9, "bold")); s.configure("Treeview", font=("Arial", 9), rowheight=28); Bank(r); r.mainloop()