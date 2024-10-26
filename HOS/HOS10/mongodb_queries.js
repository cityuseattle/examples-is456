// Select the database to use.
use('mongodbVSCodePlaygroundDB');
// Insert a new country into the countries collection
db.countries.insertOne({
  name: "Wakanda",
  continent: "Africa",
  population: 1000000,
  capital: "Birnin Zana"
});

// Verification: Check if the new country was added:
db.countries.find({ name: "Wakanda" });

// Find all countries in Africa:
db.countries.find({ continent: "Africa" });

// Update the population of Wakanda:
db.countries.updateOne(
  { name: "Wakanda" },
  { $set: { population: 1500000 } }
);

// Verification: Check if the population update is reflected:
db.countries.find({ name: "Wakanda" });


// Delete the country "Wakanda":
db.countries.deleteOne({ name: "Wakanda" });

// Verification: Confirm the deletion:

db.countries.find({ name: "Wakanda" });
