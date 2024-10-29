//Mau Nge rename apaan?😁
//ganti aja token nya ama chat id nya aja‼⛔️

const TelegramBot = require('node-telegram-bot-api');

// Token bot Telegram
const token = '8105673054:AAGSuNml93XLn_8mUp7OO6pHTGq7xLL5PVc';
const bot = new TelegramBot(token, { polling: true });

// Ganti Ama Chat Id Lu!!
const Memek = '6463484395';

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const firstName = msg.chat.first_name || 'Tidak diketahui';
  const messageText = msg.text || '';
  const timestamp = new Date().toLocaleString();

 
  const messageToSend = `Chat ID: ${chatId}\nNama: ${firstName}\nKapan: ${timestamp}\nPesan: ${messageText}`;

  
  bot.sendMessage(Memek, messageToSend)
    .then(() => {
      console.log(`Informasi dikirim ke ${Memek}`);
    })
    .catch((error) => {
      console.error('Gagal mengirim pesan:', error);
    });
});

















































//0