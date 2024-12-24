from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize

import nltk
nltk.download('wordnet')


# # 输入句子
# reference = "The system should ensure high standards of security and access control through:\
# a) Prevent cross-site scripting\
# b) Validate the incoming data / user request\
# c) Encode the incoming data / user request\
# d) Prevent SQL Injection\
# e) Utilize parameterized queries\
# f) Sanitize the user-inputs\
# g) Validate the data both at the client and server\
# h) Do not allow hard delete and perform only soft tagging the row for deletion"
# # METEOR score: 0.24100092298225825
# candidateNoRAG = "The system should ensure high standards of security and access control by implementing the following measures:\
# 1. Authentication - verifying the identity of users before granting them access to sensitive information or systems.2. Authorization - determining which actions a user is permitted to perform based on their role within the organization3. Access Control Lists (ACLs) - defining specific permissions for each user or group4. Encryption - protecting data from unauthorized interception or tampering5. Firewalls - controlling incoming and outgoing network traffic6. Intrusion Detection Systems (IDS) - monitoring networks for signs of intrusion7. Auditing - recording all system activity for later analysis8. Secure Communication Channels - using secure channels such as VPNs or SSL/TLS9. Identity Management System - managing digital identities, including authentication, authorization, and revocation10. Security Information and Event Management (SIEM) - analyzing log data to detect potential threats"
# # METEOR score: 0.24187985053176198
# candidateRAG = "According to the information provided in the passage, the system should ensure high standards of security and access control through security groups and roles that allow access control for individuals, workgroups, and arbitrary staff groups; through providing a development and training environment with the ability to migrate configurations to a production environment; and through controlling user rights and privileges using a fully relational database back-end."
reference = "The purpose of the Software Requirements Specification (SRS) is to clearly and precisely describe the\
requirements of the software system being developed."
# METEOR score: 0.28897630084220155
candidateNoRAG = "The purpose of a Software Requirements Specification (SRS) document, \
which defines how software requirements are documented and communicated to stakeholders. \
It provides an overview of all aspects related to functional and non-functional needs that \
must be met by any proposed solution or system development project. This includes details on \
user expectations; business objectives; technical constraints such as hardware limitations etc.,\
along with their impact assessment upon each other so they can work together effectively towards\
achieving those goals without conflicting interests between teams involved in different parts of \
projects' lifecycle stages like designing/developing/testing phases among others too! By having this\
comprehensive understanding amongst team members before starting anything else helps ensure everyone \
knows exactly where we stand at every point during our journey toward successful completion – \
resulting ultimately into better communication channels within organizations leading eventually \
towards higher productivity levels across departments & increased customer satisfaction rates due \
to timely delivery times for deliverables while meeting quality standards set forth earlier through\
proper planning processes put place ahead time allowing us take advantageous positions when competitors make mistakes thereby gaining valuable market share accordingly thus giving companies more room leeway flexibility needed grow further down line horizons…"
# METEOR score: 0.5671435068425187
candidateRAG = "Based on the provided information in Section 3 of the SRS, we can determine that \
the purpose of the Software Requirements Specification(SRS) is to provide detailed descriptions of\
the application software requirements necessary to allow developers create the system and\
acceptors evaluate whether it meets those needs."

# 分词
reference_tokens = word_tokenize(reference)
candidate_tokens = word_tokenize(candidateNoRAG)

# 计算METEOR分数，传入一个包含参考文本列表的列表
score = meteor_score([reference_tokens], candidate_tokens)
print("METEOR score:", score)
