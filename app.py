import streamlit as st
import pandas as pd


st.markdown("""
 🌍 The Future of Work

Modern teams face increasing workloads, tight deadlines,
and difficulties in prioritizing tasks.

WorkFlow AI uses intelligent decision-support principles
to help workers and teams organize work, identify risks,
and make better decisions.
""")

st.set_page_config(
    page_title="WorkFlow AI",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 WorkFlow AI")
st.caption("Turn work chaos into intelligent action.")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a page",
    [
        "🏠 Dashboard",
        "📋 AI Work Planner",
        "⚠️ Risk Detector",
        "👥 Workload Analyzer"
    ]
)


if page == "🏠 Dashboard":

    st.header("📊 Work Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tasks", "0")
    col2.metric("High Priority", "0")
    col3.metric("Project Risks", "0")
    col4.metric("Team Members", "0")

    st.info(
        "👋 Welcome to WorkFlow AI. "
        "Use the navigation menu to plan and analyze your work."
    )

elif page == "📋 AI Work Planner":

    st.header("📋 AI Work Planner")

    st.write(
        "Describe your project and WorkFlow AI will help "
        "you organize your work."
    )

    project_description = st.text_area(
        "Describe your project",
        placeholder="""
Example:

We need to develop a website for a small business.
We have five days to complete the project.
The project requires research, design, development,
testing and a final presentation.
"""
    )

    if st.button("✨ Generate Work Plan"):

        if project_description:

            st.success("Work plan generated!")

            data = {
                "Task": [
                    "Research project requirements",
                    "Plan the solution",
                    "Design the system",
                    "Develop the solution",
                    "Test the system",
                    "Prepare final presentation"
                ],
                "Priority": [
                    "High",
                    "High",
                    "High",
                    "High",
                    "Medium",
                    "Medium"
                ],
                "Suggested Deadline": [
                    "Day 1",
                    "Day 1",
                    "Day 2",
                    "Day 4",
                    "Day 5",
                    "Day 5"
                ]
            }

            df = pd.DataFrame(data)

            st.subheader("📋 Recommended Tasks")

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader("🧠 AI Recommendation")

            st.info(
                "Start with project requirements and planning. "
                "Begin design early so development can start as soon as possible."
            )

        else:

            st.warning(
                "Please enter a project description."
            )


elif page == "⚠️ Risk Detector":

    st.header("⚠️ Project Risk Detector")

    number_tasks = st.number_input(
        "How many tasks does your project have?",
        min_value=1,
        value=5
    )

    days_remaining = st.number_input(
        "How many days remain?",
        min_value=1,
        value=5
    )

    if st.button("🔍 Analyze Project Risk"):

        workload = number_tasks / days_remaining

        st.subheader("Risk Analysis")

        st.write(
            f"Average tasks per day: {workload:.1f}"
        )

        if workload >= 5:

            st.error(
                "🔴 HIGH RISK: "
                "Your workload may be too high for the available time."
            )

            st.write(
                "### Recommendation"
            )

            st.write(
                "- Prioritize critical tasks"
            )

            st.write(
                "- Delegate work where possible"
            )

            st.write(
                "- Start high-priority tasks immediately"
            )

        elif workload >= 3:

            st.warning(
                "🟡 MEDIUM RISK: "
                "Your project requires careful planning."
            )

        else:

            st.success(
                "🟢 LOW RISK: "
                "Your workload appears manageable."
            )

elif page == "👥 Workload Analyzer":

    st.header("👥 Team Workload Analyzer")

    st.write(
        "Enter the number of tasks assigned to each team member."
    )

    member1 = st.number_input(
        "Tasks assigned to Team Member 1",
        min_value=0,
        value=0
    )

    member2 = st.number_input(
        "Tasks assigned to Team Member 2",
        min_value=0,
        value=0
    )

    member3 = st.number_input(
        "Tasks assigned to Team Member 3",
        min_value=0,
        value=0
    )

    if st.button("📊 Analyze Workload"):

        workloads = [
            member1,
            member2,
            member3
        ]

        average = sum(workloads) / len(workloads)

        st.subheader("📊 Workload Results")

        df = pd.DataFrame({
            "Team Member": [
                "Member 1",
                "Member 2",
                "Member 3"
            ],
            "Tasks": workloads
        })

        st.dataframe(
            df,
            use_container_width=True
        )

        maximum = max(workloads)
        minimum = min(workloads)

        if maximum - minimum >= 3:

            st.warning(
                "⚠️ Workload imbalance detected!"
            )

            overloaded_index = workloads.index(maximum) + 1

            st.write(
                f"Team Member {overloaded_index} "
                "has significantly more work than other members."
            )

            st.info(
                "💡 Recommendation: Redistribute some tasks "
                "to balance the workload."
            )

        else:

            st.success(
                "✅ Workload appears reasonably balanced."
            )