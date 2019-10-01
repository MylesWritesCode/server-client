// Pipeline for find_SMA_50(float high, float low).
var low = 0.00;
var high = 0.01;

var pipeline = [
  {
    $project: {
      "_id": 0,
      "Ticker": 1,
      "50-Day Simple Moving Average": 1
    }
  },
  {
    $match: {
      "50-Day Simple Moving Average": {
          "$gt": low,
          "$lt": high
      }
    }
  },
  {
    $group: {
        "_id": null,
        "count": { $sum: 1 }
    }
  }
]

// Pipeline for find_industry(string industry).
var industry = "Medical Laboratories & Research";

var pipeline = [
  {
      $project: {
        "_id": 0,
        "Ticker": 1,
        "Industry": 1
      }
  },
  {
      $match: {
        "Industry": industry
      }
  },
  {
      $group: {
        "_id": null,
        "Tickers": { $push: "$Ticker" }
      }
  }
]

// Pipeline for find_outstanding_shares_by_sector(string sector).
var sector = "Healthcare";
var pipeline = [
  {
    $project: {
      "_id": 0,
      "Sector": 1,
      "Industry": 1,
      "Shares Outstanding": 1
    }
  },
  {
    $match: {
      "Sector": sector
    }
  },
  {
    $group: {
      "_id": "$Industry",
      "Total Outstanding Shares": { $sum: "$Shares Outstanding" }
    }
  }
]