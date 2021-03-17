export interface BenchmarkSummaryModel {
  upd_date: string;
  toscana: {
    ti_percentage: number;
    ti_perc_increment: number;
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  veneto: {
    ti_percentage: number;
    ti_perc_increment: number;
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  marche: {
    ti_percentage: number;
    ti_perc_increment: number;
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
}
