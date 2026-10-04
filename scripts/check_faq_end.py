with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="faq"')
end_sec = text.find('</section>', idx)
print("End of #faq </section>:", end_sec)
print(text[end_sec:end_sec+300])
