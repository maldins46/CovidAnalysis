export interface MarcheSummaryModel {
  upd_date: string;
  pesaro_e_urbino: {
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  macerata: {
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  fermo: {
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  ascoli_piceno: {
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
  ancona: {
    new_positives: number;
    perc_increment_on_yesterday: number;
    perc_increment_on_4_weeks: number;
  };
}
