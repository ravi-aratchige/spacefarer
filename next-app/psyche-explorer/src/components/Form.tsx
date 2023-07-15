export default function Form() {
    return (
        <form action="">
            <h1>Openness</h1>
            <label htmlFor="">Agree</label>
            <input type="radio" name="q1" value="5" />
            <input type="radio" name="q1" value="4" />
            <input type="radio" name="q1" value="3" />
            <input type="radio" name="q1" value="2" />
            <input type="radio" name="q1" value="1" />
            <label htmlFor="">Disagree</label>

            <h1>Conscientiousness</h1>
            <label htmlFor="">Agree</label>
            <input type="radio" name="q2" value="5" />
            <input type="radio" name="q2" value="4" />
            <input type="radio" name="q2" value="3" />
            <input type="radio" name="q2" value="2" />
            <input type="radio" name="q2" value="1" />
            <label htmlFor="">Disagree</label>

            <h1>Extraversion</h1>
            <label htmlFor="">Agree</label>
            <input type="radio" name="q3" value="5" />
            <input type="radio" name="q3" value="4" />
            <input type="radio" name="q3" value="3" />
            <input type="radio" name="q3" value="2" />
            <input type="radio" name="q3" value="1" />
            <label htmlFor="">Disagree</label>

            <h1>Agreeableness</h1>
            <label htmlFor="">Agree</label>
            <input type="radio" name="q4" value="5" />
            <input type="radio" name="q4" value="4" />
            <input type="radio" name="q4" value="3" />
            <input type="radio" name="q4" value="2" />
            <input type="radio" name="q4" value="1" />
            <label htmlFor="">Disagree</label>

            <h1>Neuroticism</h1>
            <label htmlFor="">Agree</label>
            <input type="radio" name="q5" value="5" />
            <input type="radio" name="q5" value="4" />
            <input type="radio" name="q5" value="3" />
            <input type="radio" name="q5" value="2" />
            <input type="radio" name="q5" value="1" />
            <label htmlFor="">Disagree</label>

            <br />

            <button type="submit">Submit</button>
        </form>
    );
}