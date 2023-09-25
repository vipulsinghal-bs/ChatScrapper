const puppeteer = require('puppeteer');
const { filterList } = require('./text-summary');

(async () => {
  const browser = await puppeteer.launch({ headless: true }); // Launch a headful browser for testing
  const page = await browser.newPage();

  const navigationPromise = page.waitForNavigation()

  await page.goto('https://accounts.google.com/ServiceLogin?continue=https://chat.google.com/?referrer=2', { waitUntil: 'domcontentloaded' });

  await navigationPromise

  await page.type('input[type="email"]', 'vipul.singhal@bigsteptech.com');
  await page.waitForSelector('#identifierNext')
  await page.click('#identifierNext');

  await navigationPromise

  await page.waitForSelector('input[type="password"]');
  await page.click('input[type="password"]')
  await page.type('input[type="password"]', 'vipul@bigstep');

  await page.waitForSelector('#passwordNext')
  await page.click('#passwordNext')  

  await page.setDefaultTimeout(30000);
  await page.waitForTimeout(20000)

  page.goto('https://mail.google.com/chat/u/0/#chat/space/AAAAshUm0uo')

  await navigationPromise

  // await page.evaluate(() => {
  //   window.scrollBy(0, -500); // Adjust the scroll amount as needed (from sudhir)
  // });

  const iframeHandle = await page.waitForSelector('iframe[title="Chat content"]');
  const frame = await iframeHandle.contentFrame();

  // Find the div element inside the iframe and extract its text content

  // const divText = await frame.evaluate(() => {
  //   const div = document.querySelector('div[jsname="bgckF"]');
  //   return div ? div.textContent.trim() : null;
  // });

  const divTexts = await frame.evaluate(() => {
    const divs = document.querySelectorAll('div[jsname="bgckF"]');
    return Array.from(divs).map((div) => div.textContent.trim());
  });

  // let reachedTarget = false;                      // from sudhir
  // await frame.click('div[class="cK9mzf"]');  
  // while (!reachedTarget) {
  //   await frame.focus('body');
  //   for(let i = 0;i<3;i++) {
  //     await frame.page().keyboard.press('ArrowUp')
  //   }
  //   const isTargetVisible = await frame.evaluate(() => {
  //     const targetElement = document.querySelector('div[class="cK9mzf"]'); // Replace with the selector of your target element
  //     const topElement = document.querySelector('button[aria-label="Add people & apps to this space"]');
  //     if (targetElement || topElement) {
  //       const dateString = targetElement.textContent;
  //       const year = 2023; // You can change this to any desired year
  //       const dateStringWithYear = dateString + `, ${year}`;
  //       const specificDate = dateString != 'Yesterday' && dateString != 'Today' ? new Date(dateStringWithYear): new Date();
  //       return specificDate <= new Date('Friday, June 02' + `, ${year}`) || topElement;
  //     }
  //     return false;
  //   });

  //   if (isTargetVisible) {
  //     reachedTarget = true;
  //     console.log('Reached the target text "Mon 18 Sep".');
  //   }
  // }
  // const divText = await frame.evaluate(async () => {
  //   // debugger
  //   let namesNodes = document.querySelectorAll('div[jsname="A9KrYd"]');
  //   let messagesNodes = document.querySelectorAll('div[class="Hj5Fxb"]');
  //   let title = document.title;
  //   let names = [];
  //   let messages = [];
  //   for(let i = 0;i< messagesNodes.length;i++) {
  //     const text = messagesNodes[i].firstElementChild.textContent.trim()
  //     const imgSrc = messagesNodes[i].getElementsByClassName('HQLhSc').length != 0? messagesNodes[i].getElementsByClassName('HQLhSc')[0].src: null;
  //     messages.push({text, imgSrc, name: namesNodes[i].textContent.trim()});
  //   }
  //   return messages;
  // });
    
  // if (divText !== null) {
  //   console.log('Text content of the div inside the iframe:', divText);
  //   // const newsletterHTML = generateNewsletterHTML(divText);
  // } else {
  //   console.log('Div element not found inside the iframe.');
  // }

  divTexts.forEach((text, index) => {
      console.log(`Text content of div ${index + 1}: ${text}`);
    });

  filterList(divTexts);

    
  // Extract messages (this is just a basic example, you'll need to refine it).
  // const messages = await page.evaluate(() => {
  //   const messageElements = document.querySelectorAll('div[role="listitem"]'); // Adjust the selector as needed.
  //   const messages = [];

  //   for (const messageElement of messageElements) {
  //     const sender = messageElement.querySelector('span[aria-label="Sender name"]').textContent;
  //     const messageText = messageElement.querySelector('div[data-message-id]').textContent;
  //     const timestamp = messageElement.querySelector('div[role="timer"]').getAttribute('title');

  //     messages.push({ sender, messageText, timestamp });
  //   }

  //   return messages;
  // });

  // console.log(messages);

  await browser.close();
})();
