## 📜 Tasks List & Details

---

### **Task 01: Research on Generative AI** ✅
**Objective:**  
An overview of Generative AI, including how it works, key concepts like **deep learning**, **transformers**, and **diffusion models**, plus applications in **text, image, and audio** generation.

**What I Did:**  
- Studied working principles and architectures.
- Wrote a blog simplifying concepts for beginners.
- Created example Python files demonstrating text/image generation.

🔗 **GitHub Folder**: [`01GenAi`](./01GenAi)  
📝 **Medium Blog**: [What is AI and Generative AI – A Beginner’s Guide](https://medium.com/@shuremsyed41/what-is-ai-and-generative-ai-a-complete-beginners-guide-1bdf9df6917b)
**✅ Status:** Completed
---

### **Task 02: Learn About FastAPI** ✅
**Objective:**  
Introduction to **FastAPI**, a modern Python framework for building efficient APIs with async support, automatic docs, and type hints.

**What I Did:**  
- Studied Panaverse FastAPI material.
- Built small APIs locally to understand structure.
- Tested async endpoints.

🔗 **GitHub Folder**: [`02Fastapi`](./02Fastapi)  
📖 **Original Resource**: [FastAPI Intro - Panaverse](https://github.com/panaversity/learn-agentic-ai/tree/main/04_daca_agent_native_dev/01_intro_fastapi)
**✅ Status:** Completed
---

### **Task 03: Pydantic** ✅
**Objective:**  
Learn Pydantic for **data validation** and **type enforcement** in Python.

**What I Did:**  
- Used `BaseModel`, `EmailStr`, and `constr` for validation.
- Tested validation failures & success cases.


🔗 **GitHub Folder**: [`03Pydantic`](./03Pydantic)  
📖 **Reference**: [Pydantic Validation - Panaverse](https://github.com/panaversity/learn-agentic-ai/blob/main/04_daca_agent_native_dev/01_intro_fastapi/02_pydantic_validation/readme.md)
**✅ Status:** Completed
---
---

### **Task 04: FastAPI Parameters** ✅
**Objective:**  
Use **query parameters**, **path parameters**, and **request bodies** in FastAPI.

**What I Did:**  
- Practiced `Path`, `Query`, and `Body` imports.
- Added constraints like min/max values.


🔗 GitHub Folder: 04Fastapi_parameters
📖 Original Resource: API Parameters - Panaverse
**✅ Status:** Completed


### **Task 05: Dependency Injection in FastAPI** ✅
**Objective:**  
Understand FastAPI’s built-in **dependency injection** system.

**What I Did:**  
- Passed shared resources like DB connections into endpoints.
- Created reusable auth & config dependencies.

🔗 Folder: [`05Dependency_Injection`](./05Dependency_Injection)
**✅ Status:** Completed
---

### **Task 06: Task Tracker API** ✅
**Objective:**  
Build an API that manages **Users** and **Tasks** with Pydantic validation.

**What I Did:**  
- Models: `UserCreate`, `UserRead`, `Task`.
- Endpoints: CRUD for users & tasks.
- Validations: Email format, username length, due date ≥ today.

🔗 Folder: [`06Task_Tracker_API`](./06Task_Tracker_API)
**✅ Status:** Completed
---

### **Task 07: OpenAI Agent SDK** ✅
**Objective:**  
Learn to build **AI Agents** using OpenAI’s SDK.

**What I Did:**  
- Registered tools.
- Implemented basic agent execution.

🔗 Folder: [`07OpenAI_Agent_SDK`](./07OpenAI_Agent_SDK)
**✅ Status:** Completed
---

### **Task 08: What is an LLM?** ✅
**Objective:**  
Explain **Large Language Models** – what they are, how they work, and real-world uses.

**What I Did:**  
- Compared GPT-like models.
- Connected concepts to ChatGPT.

🔗 Folder: [`08LLM`](./08LLM)
**✅ Status:** Completed
---

### **Task 09: What is Function / Tool Calling?** ✅
**Objective:**  
Research how **function/tool calling** works and powers agents.

**What I Did:**  
- Wrote examples of calling external APIs via agents.
- Compared use cases with normal prompts.

🔗 Folder: [`09Function_Tool_Calling`](./09Function_Tool_Calling)
**✅ Status:** Completed
---

### **Task 10: Crypto Market Rate Agent** ✅
**Objective:**  
Create an agent to fetch current crypto market rates.

**What I Did:**  
- Used Binance & CoinLore APIs.
- Integrated into agent workflow.

🔗 Folder: [`10Crypto_Agent`](./10Crypto_Agent)
**✅ Status:** Completed
---

### **Task 11: Inner Working of Function Tools** ✅
**Objective:**  
Understand inner functioning of tool-calling inside agents.

**What I Did:**  
- Explored docstrings and function tool responses.
- Tested prompts like:
  - Weather queries.
  - Restaurant searches.
  - Sending emails & scheduling meetings.

🔗 Folder: [`11Inner_Working_Function_Tools`](./11Inner_Working_Function_Tools)
**✅ Status:** Completed
---

### **Task 12: Hands-On on Hands-Off** ✅
**Objective:**  
Create poetry agents & analysts.

**What I Did:**  
- Made **Poet Agent**.
- Three **Analyst Agents**.
- One **Triage Agent** that routes to the correct analyst.

🔗 Folder: [`12Hands_On_Hands_Off`](./12Hands_On_Hands_Off)
**✅ Status:** Completed  
---

## 📌 Class Assignments

### Translator Agent ✅
- Built simple translator agent for multiple languages.
**✅ Status:** Completed
### Crypto Agent ✅
- Same as Task 10 but implemented in class.
**✅ Status:** Completed
### Shopping Agent ⏳ (Pending)  
- Will use product API with tool calling.
**✅ Status:** Completed
### Input Guardrails ✅
- Class timing change guardrail.
- Father temperature restriction guardrail.
- Gatekeeper school access guardrail.
**✅ Status:** Completed
---
## 📌 Context Management (Agent SDK) ✅

### **Objective**
Practice using **OpenAI Agent SDK**'s **Local Context Management** feature to handle contextual data during agent execution.

---

### **What I Did**
- Created **Pydantic models** for different context types:
  - **Bank Account**
  - **Student Profile**
  - **Library Book**
- Passed these models as **context** to the agent using `RunContextWrapper`.
- Registered tools to read and display contextual data.
- Ran and verified that the agent used context in responses.

---

### **Example Code**
```python
# 1. BANK ACCOUNT CONTEXT
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Fatima Khan",
    account_balance=75500.50,
    account_type="savings"
)

# 2. STUDENT PROFILE CONTEXT
student = StudentProfile(
    student_id="STU-456",
    student_name="Hassan Ahmed",
    current_semester=4,
    total_courses=5
)

# 3. LIBRARY BOOK CONTEXT
library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)
```
---

🔗 Folder: [`ContextManagement`](./ContextManagement)
**✅ Status:** Completed
  

---

## 🚀 Next Steps  
- ✅ Complete **Shopping Agent**  
- 🔄 Work on **multi-agent orchestration** and **context management** improvements  

---

## 🙌 About Me  
**👤 Name:** Syed Shurem Ali  

### 🌐 Social Links  
- 💼 [LinkedIn](https://www.linkedin.com/in/syed-shurem-ali-5a55852a0)  
- 🐙 [GitHub](https://github.com/) *(Add your username)*  
- 📧 **Email:** *(shuremsyed41@gmail.com)*  

---

> _"Learning by doing is the best way to grow — and I’m just getting started!"_

---
