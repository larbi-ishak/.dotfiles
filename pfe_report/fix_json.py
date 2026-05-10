with open("pfe_report/main.tex", "r") as f:
    content = f.read()

# JSON is not natively supported by listings out of the box in this setup without explicit definition.
# We will change it to 'bash' or remove the language requirement.
new_content = content.replace("lstlisting}[language=json,", "lstlisting}[language=bash,")

with open("pfe_report/main.tex", "w") as f:
    f.write(new_content)
