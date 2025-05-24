// Dummy AI function for demonstration. Replace with real API call.
async function call_gpt(prompt) {
  // Simulate AI response
  if (prompt.includes("possible cases")) {
    return [
      "Common Cold",
      "Flu",
      "COVID-19"
    ];
  }
  if (prompt.includes("more information about case #")) {
    return "Flu: lasts 5-7 days, treat with rest and fluids.";
  }
  if (prompt.includes("How urgent")) {
    return "See a doctor if symptoms worsen or high fever persists.";
  }
  return "No data.";
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const symptoms = document.getElementById('symptoms').value.trim();
    const duration = document.getElementById('duration').value.trim();
    const resultsDiv = document.getElementById('results');

    if (!symptoms || !duration) {
      resultsDiv.textContent = "Please enter both symptoms and duration.";
      return;
    }

    resultsDiv.textContent = "Analyzing...";

    // Step 1: Get possible cases
    const possible_cases = await call_gpt(`What are all the possible cases from most likely to least likely for a person who has ${symptoms} as symptoms that has lasted ${duration} long?`);

    // Step 2: Pick the most likely case (for demo, pick the first)
    const selected_case_number = 1;
    const selected_case = possible_cases[0];

    // Step 3: Get more info about the selected case
    const selected_case_details = await call_gpt(`Give me more information about case #${selected_case_number} from the ${JSON.stringify(possible_cases)}, such as how long it lasts, and how to treat it.`);

    // Step 4: Get emergency advice
    const emergency_advice = await call_gpt(`How urgent is a situation if someone has had ${selected_case} from the ${JSON.stringify(possible_cases)} for ${duration}? Should they see a doctor immediately, call 911, or what?`);

    // Step 5: Build JSON resulthelp
    const result = {
      symptoms,
      duration,
      possible_cases,
      selected_case_number,
      selected_case_details,
      emergency_advice
    };

    // Step 6: Display result
    resultsDiv.textContent = JSON.stringify(result, null, 2);
  });
});