
export class DateUtils {
  static readonly MILLIS_IN_SECOND = 1000;
  static readonly SECONDS_IN_MINUTES = 60;
  static readonly MINUTES_IN_HOUR = 60;
  static readonly HOURS_IN_DAYS = 24;
  static readonly MILLIS_IN_DAY = DateUtils.MILLIS_IN_SECOND * DateUtils.SECONDS_IN_MINUTES *
    DateUtils.MINUTES_IN_HOUR * DateUtils.HOURS_IN_DAYS;

  static addDaysToToday(days: number): Date {
    const newDate = new Date();
    newDate.setDate(new Date().getDate() + days);
    return newDate;
  }

  static addHoursToNow(hours: number): Date {
    const newDate = new Date();
    newDate.setHours(new Date().getHours() + hours);
    return newDate;
  }

  static addDay(date: Date): Date {
    const newDate = new Date(date);
    newDate.setDate(date.getDate() + 1);
    return newDate;
  }

  static twoDaysBefore(date: Date): Date {
    const newDate = new Date(date);
    newDate.setDate(date.getDate() - 2);
    newDate.setHours(0, 0, 0, 0);
    return newDate;
  }
}
