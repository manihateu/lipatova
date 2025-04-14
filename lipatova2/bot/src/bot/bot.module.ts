/* eslint-disable prettier/prettier */
import { Module } from '@nestjs/common';
import { TelegrafModule } from 'nestjs-telegraf';
import { BotService } from './bot.service';

@Module({
  imports: [
    TelegrafModule.forRoot({
      token: '7716605822:AAH0xrccjFpjYg_h8XgsMaxPf20i2FwxDfc',
    }),
  ],
  providers: [BotService],
})
export class BotModule {}
