/* eslint-disable prettier/prettier */
import { Injectable } from '@nestjs/common';
import { InjectBot } from 'nestjs-telegraf';
import { Telegraf, Context, Markup } from 'telegraf';

@Injectable()
export class BotService {
  constructor(@InjectBot() private readonly bot: Telegraf) {
    this.bot.start((ctx) => this.start(ctx));
    this.bot.command('recommend', (ctx) => this.askApplicationType(ctx));
    this.bot.action('web', (ctx) => this.handleWeb(ctx));
    this.bot.action('mobile', (ctx) => this.handleMobile(ctx));
    this.bot.action('beginner', (ctx) => this.handleBeginner(ctx));
    this.bot.action('expert', (ctx) => this.handleExpert(ctx));
    this.bot.action('desktop', (ctx) => this.handleDesktop(ctx));
    this.bot.action('data', (ctx) => this.handleData(ctx));
    this.bot.action('games', (ctx) => this.handleGames(ctx));
  }

  start(ctx: Context) {
    ctx.reply(
      'Привет! Я помогу выбрать язык программирования. Нажмите /recommend, чтобы начать.',
    );
  }

  askApplicationType(ctx: Context) {
    ctx.reply(
      'Выберите тип приложения:',
      Markup.inlineKeyboard([
        Markup.button.callback('Web', 'web'),
        Markup.button.callback('Мобильное', 'mobile'),
        Markup.button.callback('Десктопное', 'desktop'),
        Markup.button.callback('Анализ данных', 'data'),
        Markup.button.callback('Игры', 'games'),
      ]),
    );
  }

  handleWeb(ctx: Context) {
    ctx.reply('Вы выбрали Web-приложение.');
    ctx.replyWithPhoto(
      {
        url: 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
      },
      { caption: 'JavaScript — популярный выбор для веб-разработки.' },
    );
    ctx.reply(
      'Какой уровень квалификации?',
      Markup.inlineKeyboard([
        Markup.button.callback('Начинающий', 'beginner'),
        Markup.button.callback('Эксперт', 'expert'),
      ]),
    );
  }

  handleMobile(ctx: Context) {
    ctx.reply('Вы выбрали Мобильное приложение.');
    ctx.replyWithPhoto(
      {
        url: 'https://upload.wikimedia.org/wikipedia/commons/0/06/Kotlin-logo.png',
      },
      { caption: 'Kotlin — отличный выбор для Android-разработки.' },
    );
    ctx.reply(
      'Какой уровень квалификации?',
      Markup.inlineKeyboard([
        Markup.button.callback('Начинающий', 'beginner'),
        Markup.button.callback('Эксперт', 'expert'),
      ]),
    );
  }

  handleDesktop(ctx: Context) {
    ctx.reply('Вы выбрали Десктопное приложение.');
    ctx.reply(
      'Для десктопных приложений рекомендуется C# или Python. Документация: https://docs.microsoft.com/ru-ru/dotnet/csharp/',
    );
  }

  handleData(ctx: Context) {
    ctx.reply('Вы выбрали Анализ данных.');
    ctx.reply(
      'Для анализа данных рекомендуется Python. Документация: https://www.python.org/doc/',
    );
  }

  handleGames(ctx: Context) {
    ctx.reply('Вы выбрали Игры.');
    ctx.reply(
      'Для разработки игр рекомендуется C++. Документация: https://en.cppreference.com/',
    );
  }

  handleBeginner(ctx: Context) {
    ctx.reply(
      'Для начинающих разработчиков рекомендуется Python. Документация: https://www.python.org/doc/.',
    );
  }

  handleExpert(ctx: Context) {
    ctx.reply(
      'Для экспертов рекомендуется Rust. Документация: https://doc.rust-lang.org/book/.',
    );
  }
}
